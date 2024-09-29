from random import choices, choice, shuffle
from src.players.football_player import FootballPlayer
from src.team.football_team import FootballTeam
from src.balancer import TeamBalancer
from src.enums.positions import FootballPositions


class SquadMaker:

    def __init__(self, players: list[FootballPlayer]):
        #TODO: VALIDATION
        self.player_record = players
        shuffle(players)
        self.players = players
        self._root_team_name = "TEAM"
        self.balancer = TeamBalancer()

    def __call__(self, pos_slots: dict, team_no: int = 2) -> dict[int, FootballTeam]:
        team_names = [f"{self._root_team_name}_{nb}" for nb in range(team_no)]
        assigned_teams = {name: self._create_team(name, pos_slots) for name in team_names}
        updated_teams = self.balancer(assigned_teams)
        return updated_teams
    
    def _create_team(self, team_name, pos_slots) -> FootballTeam:
        players_by_position = self._assign_players(pos_slots)
        return FootballTeam(team_name, players_by_position)
    
    def _assign_players(self, slot_dist: dict) -> dict:
        assigned_players = dict()
        empty_positions = 0
        for position, slots in slot_dist.items():
            assigned_players_on_position, left_quota = self._assign_position_wise(position, slots)
            assigned_players.update({position: assigned_players_on_position})
            empty_positions += left_quota
        self._assign_rest_randomly(empty_positions)
        return assigned_players
    
    def _assign_rest_randomly(self, assigned_players: dict[FootballPositions, list[FootballPlayer]], empty_positions: int) -> None:
        if empty_positions:
            chosen_players: list[FootballPlayer] = choices(self.players, k=empty_positions)
            for player in chosen_players:
                position = choice(list(player.position_scores.keys()))
                self.players.remove(player)
                assigned_players[position].append(player)

    def _create_priority(self, position: FootballPositions, quota: int) -> tuple[list[FootballPlayer], int]: 
        primary, secondary = list(), list()
        for player in self.players:
            if not quota:
                break
            if position in player.position_scores:
                if len(player.position_scores) == 1:
                    primary.append(player)
                    quota -= 1
                else:
                    secondary.append(player)
        for ps in secondary:
            if not quota:
                break
            primary.append(ps)
            quota -= 1
        return primary, quota
        
    def _assign_position_wise(self, position: FootballPositions, quota: int) -> tuple[list[FootballPlayer], int]:
        assigned_players = list()
        allocable_players, left_quota = self._create_priority(position, quota)
        if left_quota:
            occupied_quata = quota - left_quota
            quota -= occupied_quata
        self._assign_free_players(assigned_players, allocable_players, quota)
        return assigned_players, left_quota
    
    def _assign_free_players(self, assigned_players: list, allocable_players: list, quota: int) -> None:
        i = 0
        while i <= quota and i < len(allocable_players):
            player = allocable_players[i]
            assigned_players.append(player)
            self.players.remove(player)
            i += 1