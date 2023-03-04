from src.team.abs_team import AbstractTeam
from dataclasses import dataclass
from src.positions.football_positions import FootballPositions


@dataclass
class FootballTeam(AbstractTeam):
    
    def __init__(self, team_name, positions, positions_constraints):
        super().__init__(team_name, positions)
        self.positions_constraints = positions_constraints
        
    def add_player(self, Player, position):
        if self.constrain_goalkeeper(position):
            super().add_player(Player, position)
        
    def remove_player(self, Player):
        super().remove_player(Player)

    def update_team_stats(self, action: str, position_name, position_score):
        super().update_team_stats(action, position_name, position_score)

    def constrain_goalkeeper(self, position: FootballPositions):
        position_name = position.get_position_name()
        player_count = len(self.rooster[position_name])
        player_limit = self.positions_constraints[position_name]
        if player_limit is not None:
            if player_limit <= player_count:
                print(f"Player limit does not permit to assign given Player to <{position_name}> role.")
                return 0
        return 1
