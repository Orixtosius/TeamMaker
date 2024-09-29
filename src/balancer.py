from src.players.football_player import FootballPlayer
from src.team.football_team import FootballTeam
from src.enums.positions import FootballPositions


class TeamBalancer:

    def __call__(self, teams: dict[str, FootballTeam]) -> list[FootballTeam]:
        for position in FootballPositions:
            position_score = 0
            players_on_position = list()
            for team in teams.values():
                players_on_position.extend(team.rooster[position.name])
                if team.score[position.name] == position_score:
                    break
                position_score += team.score[position.name]
            else:
                updated_squad = self.balance_player_subset(players_on_position, position.name, position_score//2)
                self.update_team_scores(team, updated_squad, position.name)
        return teams

    def update_team_scores(self, team: dict[int, FootballTeam], updated_squad: list[FootballPlayer], position: FootballPositions) -> None:
        for i in range(2):
            team[i].rooster[position] = updated_squad[i]
                
    def balance_player_subset(self, players: list[FootballPlayer], position: FootballPositions,
                               target_score: float) -> tuple[list[FootballPlayer], list[FootballPlayer]]:
        players = sorted(players, reverse=True, key=lambda x: x.position_scores[position])
        subset_name = list()
        subset_score = 0
        for p in players:
            player_score = p.position_scores[position]
            if subset_score + player_score <= target_score:
                subset_name.append(p)
                players.remove(p)
                subset_score += player_score
                if subset_score + player_score == target_score:
                    break
        new_teams = players, subset_name
        return new_teams
 
    def swap_generally(self, teams: dict[str, FootballTeam]):
        pass