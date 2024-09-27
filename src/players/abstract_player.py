from abc import ABC
from src.enums.positions import FootballPositions


class AbstractPlayer(ABC):

    def __init__(self, name: str, position_scores: dict, max_score: int, min_score: int):
        self.name = name
        self.position_scores = position_scores
        self.max_score = max_score
        self.min_score = min_score

    def update_player_score(self, target_position: FootballPositions, increase_amount: int) -> None:
        temp_score = self.position_scores[target_position] + increase_amount
        if temp_score > self.max_score:
            temp_score = self.max_score
        elif temp_score < self.min_score:
            temp_score = self.min_score
        self.position_scores[target_position] = temp_score

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