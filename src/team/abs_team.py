from abc import ABC
from src.players.football_player import FootballPlayer
from src.enums.positions import FootballPositions
from src.validations.team_validation import TeamValidator


class AbstractTeam(ABC):

    def __init__(self, team_name: str, rooster: dict[FootballPositions, list] = dict()) -> None:
        self.name = team_name
        self.rooster = rooster
        self.score = dict()
        self.size = 0

    @TeamValidator()
    def add_player(self, player: FootballPlayer, position: FootballPositions) -> None:
        #TODO: ADD VALIDATION
        if player not in self.rooster[position]:
            self.rooster[position].append(player)
            player_score = player.get_score(position)
            self.update_team_stats(position, player_score)

    @TeamValidator()
    def remove_player(self, player: FootballPlayer) -> None:
        for position_name in self.rooster.keys():
            if player in self.rooster[position_name]:
                self.rooster[position_name].remove(player)
                player_score = player.get_score(position_name)
                self.update_team_stats(position_name, player_score)
                return

    def update_team_stats(self, action: str, position_name, position_score) -> None:
        count, score = self._get_values(action, position_score)
        self.size += count
        self.score[position_name] += score

    def _get_values(self, action: str, position_score: float) -> tuple[int, float]:
        if action == 'add':
            count = 1
        else:
            count = -1
        return count, count*position_score
