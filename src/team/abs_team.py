from abc import ABC
from src.players.football_player import Player
from src.enums.positions import FootballPositions
from src.validations.team_validation import TeamValidator


class AbstractTeam(ABC):

    def __init__(self, team_name: str) -> None:
        self.team_name = team_name
        self.team_score = dict()
        self.rooster: dict[FootballPositions, list] = dict()
        self.team_size = 0

    @TeamValidator()
    def add_player(self, player: Player, position: FootballPositions) -> None:
        if player not in self.rooster[position]:
            self.rooster[position].append(player)
            player_score = player.get_score(position)
            self._update_team_stats(position, player_score)
        else:
            print("The player is already in the team.")

    @TeamValidator()
    def remove_player(self, player: Player) -> None:
        for position_name in self.rooster.keys():
            if player in self.rooster[position_name]:
                self.rooster[position_name].remove(player)
                player_score = player.get_score(position_name)
                self._update_team_stats(position_name, player_score)
                break
        else:
            print("The player is not in the team.")

    def _update_team_stats(self, action: str, position_name, position_score) -> None:
        count, score = self._get_values(action, position_score)
        self.team_size += count
        self.team_score[position_name] += score
        self.total_point += score

    def _get_values(self, action: str, position_score: float) -> tuple[int, float]:
        if action == 'add':
            count = 1
        else:
            count = -1
        return count, count*position_score
