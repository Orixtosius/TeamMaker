from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Position(ABC):
    position_name: str

    @abstractmethod
    def get_position_name(self) -> str:
        return self.position_name
