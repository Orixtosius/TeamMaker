from src.players.abstract_player import AbstractPlayer
from src.positions.football_positions import FootballPositions


class Player(AbstractPlayer):

    def __init__(self, name: str, position_scores: dict, max_score: int, min_score: int):
        super().__init__(name, position_scores, max_score, min_score)

    def update_player_score(self, target_position: FootballPositions, increase_amount: int) -> None:
        super().update_player_score(target_position, increase_amount)

    def add_new_position(self, position_name: FootballPositions, score: int) -> None:
        super().add_new_position(position_name, score)

    def remove_position(self, target_position: FootballPositions) -> None:
        super().remove_position(target_position)

    def get_positions(self) -> list:
        return super().get_positions()

    def get_score(self, position):
        return super().get_score(position)
