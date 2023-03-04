from abc import ABC, abstractmethod
from src.positions.football_positions import FootballPositions


class AbstractPlayer(ABC):
    @abstractmethod
    def __init__(self, name: str, position_scores: dict, max_score: int, min_score: int):
        self.name = name
        self.position_scores = position_scores
        self.max_score = max_score
        self.min_score = min_score

    @abstractmethod
    def update_player_score(self, target_position: FootballPositions, increase_amount: int) -> None:
        temp_score = self.position_scores[target_position] + increase_amount
        if temp_score > self.max_score:
            temp_score = self.max_score
        elif temp_score < self.min_score:
            temp_score = self.min_score
        self.position_scores[target_position] = temp_score

    @abstractmethod
    def add_new_position(self, position_name: FootballPositions, score: int) -> None:
        if isinstance(position_name, FootballPositions):
            self.position_scores.update({position_name: score})
        else:
            raise TypeError(f"Given position of {position_name} is not supported.")

    @abstractmethod
    def remove_position(self, target_position: FootballPositions) -> None:
        if target_position in self.position_scores:
            self.position_scores.pop(target_position)
        else:
            raise ValueError(f"This player does not have position of {target_position}.")

    @abstractmethod
    def get_positions(self) -> list:
        return [position for position in self.position_scores.keys()]

    @abstractmethod
    def get_score(self, position):
        return self.position_scores[position]
