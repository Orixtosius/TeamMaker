from dataclasses import dataclass
from src.positions.football_positions import FootballPositions

@dataclass
class PositionEnsembler:
    positions: list

    def add_new_position(self, position_name: str) -> None:
        if isinstance(position_name, str):
            self.position_names.append(position_name)
        else:
            raise TypeError(f"Given position name type of {type(position_name)} is not supported.")

    def delete_existing_position(self, position_name: str) -> None:
        if position_name in self.position_names:
            self.position_names.remove(position_name)
        raise ValueError(f"Given position of {position_name} does not exist in position list.")

    def update_existing_position(self, existing_position_name: str, new_position_name: str) -> None:
        self.delete_existing_position(existing_position_name)
        self.add_new_position(new_position_name)

    def get_position(self, position_name):
        if position_name in self.positions:
            return FootballPositions(position_name)
        else:
            raise ValueError(f"Given position of {position_name} does not exist in position list.")