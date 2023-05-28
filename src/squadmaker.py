from dataclasses import dataclass
from src.players import Player
from src.team import Team
from src.balancer import TeamBalancer
from random import choices, choice, shuffle


@dataclass
class SquadMaker:
    rooster: list[Player] = None

    def __post_init__(self):
        self._root_team_name = "TEAM"
        self.balancer = TeamBalancer()

    def create_rooster(self, *players):
        for player in players:
            if isinstance(player, Player):
                self.rooster.append(player)
            else:
                print(f"Given player {player} is not a player.")

    def create_teams(self, pos_slots: dict, team_no: int = 2):
        self.decoy_rooster = self.rooster
        team_names = [f"{self._root_team_name}_{nb}" for nb in range(team_no)]
        assigned_teams = {name: self.build_one_team(name, pos_slots) for name in team_names}
        updated_teams = self.balancer.swap_position_wise(assigned_teams)
        return updated_teams
    
    def build_one_team(self, team_name, pos_slots):
        players_by_position = self.assign_players(pos_slots)
        return Team(team_name, self.total_team_score, players_by_position)
    
    def assign_players(self, slot_dist: dict):
        self.assigned_players = dict()
        total_empty_slots = 0
        self.total_team_score = 0
        for position, slots in slot_dist.items():
            left_quota = self.assign_players_position_wise(position, slots)
            self.assigned_players.update({position: self.assigned_players_for_position})
            total_empty_slots += left_quota
        self.assign_rest_randomly(total_empty_slots)
        return self.assigned_players
    
    def pick_up_allocable_players(self, player):
        self.decoy_rooster.remove(player)
        return player
    
    def assign_rest_randomly(self, remaining_slots):
        if remaining_slots:
            chosen_players = choices(self.decoy_rooster, k=remaining_slots)
            for player in chosen_players:
                position = choice(list(player.positions.keys()))
                self.decoy_rooster.remove(player)
                self.assigned_players[position].append(player)
                self.total_team_score += player.positions[position]

    def create_feasable_players(self, position, quota):
        
        primary, secondary = list(), list()
        shuffle(self.decoy_rooster)

        for p in self.decoy_rooster:
            if quota:
                if position in p.positions:
                    if len(p.positions) == 1:
                        primary.append(p)
                        quota -= 1
                    else:
                        secondary.append(p)
            else:
                break
        if quota:
            for ps in secondary:
                if quota:
                    primary.append(ps)
                    quota -= 1
                else:
                    break
        
        return primary, quota
        
    def assign_players_position_wise(self, position, quota):

        self.assigned_players_for_position, allocable_players = list(), list()
        allocable_players, left_quota = self.create_feasable_players(position, quota)
        if left_quota:
            quota -= quota-left_quota
        self.assign_from_feasible_candidates(allocable_players, position, quota)

        return left_quota
    
    def assign_from_feasible_candidates(self, allocable_players, position, quota):
        
        for i in range(quota):
            if i >= len(allocable_players):
                break
            player = allocable_players[i]
            self.assigned_players_for_position.append(player)
            self.decoy_rooster.remove(player)
            self.total_team_score += player.positions[position]