class Team:
    
    def __init__(self, name, score, players_by_positions):
        self.name = name
        self.score = score
        self.players_by_position, self.position_wise_score = dict(), dict()
        self.player_nbr = 0

        for position, players in players_by_positions.items():
            self.players_by_position[position] = players
            self.player_nbr += len(players)
            self.position_wise_score.update({position: sum([p.positions[position] for p in players])})

    def __repr__(self) -> str:
        repr = f"""Team named {self.name} has {self.player_nbr} players and {self.score} overall score.\n"""
        for position, players in self.players_by_position.items():
            repr += f"""{position} : \n"""
            for p in players:
                name, score = p.name, p.positions[position]
                repr += f"""{name}({score}) """
            repr += "\n"
        return repr
