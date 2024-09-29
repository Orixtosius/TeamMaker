from dataclasses import dataclass
from src.enums.positions import FootballPositions
from src.enums.scores import Scores


@dataclass
class Player:
    name: str
    positions: dict[FootballPositions, Scores]