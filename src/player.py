from dataclasses import dataclass
from src.position import Position


MAX_SCORE = 99
MIN_SCORE = 0

@dataclass
class Player:
    name: str
    position_scores: dict

    def update_player_score(self, target_position: Position, increase_amount: int) -> None:
        temp_score = self.position_scores[target_position] + increase_amount
        if temp_score > MAX_SCORE:
            temp_score = MAX_SCORE
        elif temp_score < MIN_SCORE:
            temp_score = MIN_SCORE
        self.position_scores[target_position] = temp_score

    def add_new_position(self, position_name: Position, score: int) -> None:
        if isinstance(position_name, Position):
            self.position_scores.update({position_name: score})
        else:
            raise TypeError(f"Given position of {position_name} is not supported.")

    def remove_position(self, target_position: Position) -> None:
        if target_position in self.position_scores:
            self.position_scores.pop(target_position)
        else:
            raise ValueError(f"This player does not have position of {target_position}.")

    def get_positions(self) -> list:
        return [position for position in self.position_scores.keys()]

