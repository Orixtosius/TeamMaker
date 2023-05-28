from dataclasses import dataclass
from statistics import mean
from src.team import Team
from src.positions import Positions


@dataclass
class TeamBalancer:

    def __post_init__(self):
        self.positions = Positions

    def swap_position_wise(self, teams: dict[str, Team]):
        self.teams = teams
        self.team_nbr = len(self.teams)
        if self.team_nbr != 2:
            return NotImplemented
        
        for position in self.positions:
            position_total_score = 0
            all_players_on_position = list()
            for team in self.teams.values():
                all_players_on_position.extend(team.players_by_position[position])
                if team.position_wise_score[position] == position_total_score:
                    break
                position_total_score += team.position_wise_score[position]
            else:
                subset_target_score = position_total_score//self.team_nbr
                updated_squad, updated_scores = self.balance_player_subset(
                    all_players_on_position, position, position_total_score, subset_target_score)
                self.update_team_scores(updated_squad, updated_scores, position)

        return teams

    def update_team_scores(self, updated_squad, updated_scores, position):
        for i, team in enumerate(self.teams.values()):
            team.players_by_position[position] = updated_squad[i]
            team.position_wise_score[position] = updated_scores[i]
                
    def balance_player_subset(self, players, position, position_total_score, target_score):
        players = sorted(players, reverse=True, key=lambda x: x.positions[position])
        subset_name = list()
        subset_score = 0
        for p in players:
            player_score = p.positions[position]
            if subset_score + player_score <= target_score:
                subset_name.append(p)
                players.remove(p)
                subset_score += player_score
                if subset_score + player_score == target_score:
                    break
        new_teams = players, subset_name
        new_scores = position_total_score-subset_score, subset_score
        return new_teams, new_scores
 
    def swap_generally(self, teams: dict[str, Team]):
        pass