from abc import ABC
from src.enums.positions import FootballPositions


class AbstractPlayer(ABC):

    def __init__(self, name: str, position_scores: dict):
        self.name = name
        self.position_scores = position_scores

    def update_player_score(self, target_position: FootballPositions, increase_amount: int) -> None:
        self.position_scores[target_position] = self.position_scores[target_position] + increase_amount

    def add_new_position(self, position_name: FootballPositions, score: int) -> None:
        #VALIDATE
        self.position_scores.update({position_name: score})

    def remove_position(self, target_position: FootballPositions) -> None:
        if target_position in self.position_scores:
            self.position_scores.pop(target_position)

    def get_positions(self) -> list:
        return [position for position in self.position_scores.keys()]

    def get_score(self, position: str) -> float:
        return self.position_scores[position]