from dataclasses import dataclass
from src.positions import Positions
from src.player_scores import PlayerScores
from src.utils.dict_operation import DictionaryOperator


@dataclass
class Player:
    name: str
    positions: dict[Positions, PlayerScores]


