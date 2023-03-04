from abc import ABC, abstractmethod
from functools import wraps
from src.players.football_player import Player
from src.positions.abstract_position import Position


class AbstractTeam(ABC):

    @abstractmethod
    def __init__(self, team_name, positions):
        self.team_name = team_name
        self.positions = positions
        self.team_score = dict()
        self.rooster = {p: list() for p in self.positions}
        self.total_point = 0
        self.total_player_count = 0

    def validate_player_type(method):
        @wraps(method)
        def inner(*args, **kwargs):
            if isinstance(args[1], Player):
                method(*args, **kwargs)
                return True
            else:
                print(f"Given input is not a player. It has {type(args[1])} data type.")
                return False

    @abstractmethod
    @validate_player_type
    def add_player(self, player: Player, position: Position):
        position_name = position.get_position_name()
        if player not in self.rooster[position_name]:
            self.rooster[position_name].append(player)
            player_score = player.get_score(position_name)
            self.update_team_stats(position_name, player_score)
        else:
            print("The player is already in the team.")

    @abstractmethod
    @validate_player_type
    def remove_player(self, player: Player):
        for position_name in self.rooster.keys():
            if player in self.rooster[position_name]:
                self.rooster[position_name].remove(player)
                player_score = player.get_score(position_name)
                self.update_team_stats(position_name, player_score)
                break
        else:
            print("The player is not in the team.")

    @abstractmethod
    def update_team_stats(self, action: str, position_name, position_score):
        if action == 'add':
            count = 1
            score = position_score
        elif action == 'remove':
            count = -1
            score = -position_score

        else:
            raise ValueError(f"Given <{action}> is not understood. Allowed actions are <add> or <remove>.")
        self.total_player_count += count
        self.team_score[position_name] += score
        self.total_point += score
