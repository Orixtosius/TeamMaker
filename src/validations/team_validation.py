from functools import wraps
from src.players.football_player import Player


class TeamValidator:

    def __call__(method):
        @wraps(method)
        def inner(*args, **kwargs):
            if isinstance(args[1], Player):
                return method(*args, **kwargs)
            else:
                raise TypeError(f"Given input is not a player. It has {type(args[1])} data type.")
        return inner