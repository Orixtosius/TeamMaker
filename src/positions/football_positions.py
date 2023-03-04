from dataclasses import dataclass
from src.positions.abstract_position import Position


@dataclass
class FootballPositions(Position):

    def get_position_name(self) -> str:
        return super().get_position_name()
