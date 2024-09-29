from dataclasses import dataclass
from src.team.abs_team import AbstractTeam
from src.enums.positions import FootballPositions
from src.players.football_player import FootballPlayer


@dataclass
class FootballTeam(AbstractTeam):
    
    def __post_init__(self, positions_constraints: dict = None):
        self.positions_constraints = positions_constraints
        
    def add_player(self, Player: FootballPlayer, position: FootballPositions):
        if self._is_allowed(position):
            super().add_player(Player, position)

    def _is_allowed(self, position: FootballPositions) -> bool:
        player_count = len(self.rooster[position.name])
        if self.positions_constraints is not None:
            player_limit = self.positions_constraints.get(position.name)
            if player_limit is not None:
                return player_limit > player_count
        return True