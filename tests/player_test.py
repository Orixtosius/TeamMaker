import pytest
from src.player import Player
from src.position_ensemble import PositionEnsembler


position_list = ["Goalkeeper", "Defender", "Midfielder", "Forward"]
Ensembler = PositionEnsembler(position_list)
def test_adding_position_1():
    PlayerPosition = Ensembler.get_position("Goalkeeper")
    PlayerScore = 60
    PlayerFirst = Player("Ali", {PlayerPosition: PlayerScore})
    assert PlayerFirst.position_scores[PlayerPosition] == 60

def test_adding_position_2():
    with pytest.raises(Exception) as e_info:
        PlayerPosition = Ensembler.get_position("FakePosition")
        Player("Ali", {PlayerPosition: 60})

def test_updating_score_1():
    PlayerPosition = Ensembler.get_position("Goalkeeper")
    PlayerScore = 70
    score_change = 3
    PlayerFirst = Player("Ali", {PlayerPosition: PlayerScore})
    PlayerFirst.update_player_score(PlayerPosition, score_change)
    assert PlayerFirst.position_scores[PlayerPosition] == PlayerScore + score_change

def test_updating_score_2():
    PlayerPosition = Ensembler.get_position("Goalkeeper")
    PlayerScore = 99
    score_change = 3
    PlayerFirst = Player("Ali", {PlayerPosition: PlayerScore})
    PlayerFirst.update_player_score(PlayerPosition, score_change)
    assert PlayerFirst.position_scores[PlayerPosition] == 99

def test_updating_score_3():
    PlayerPosition = Ensembler.get_position("Goalkeeper")
    PlayerScore = 99
    score_change = -3
    PlayerFirst = Player("Ali", {PlayerPosition: PlayerScore})
    PlayerFirst.update_player_score(PlayerPosition, score_change)
    assert PlayerFirst.position_scores[PlayerPosition] == 96

def test_updating_score_4():
    PlayerPosition = Ensembler.get_position("Goalkeeper")
    PlayerScore = 2
    score_change = -3
    PlayerFirst = Player("Ali", {PlayerPosition: PlayerScore})
    PlayerFirst.update_player_score(PlayerPosition, score_change)
    assert PlayerFirst.position_scores[PlayerPosition] == 0

def test_add_new_position_to_player():
    GoalkeeperPosition = Ensembler.get_position("Goalkeeper")
    DefencePosition = Ensembler.get_position("Defender")
    MidfieldPosition = Ensembler.get_position("Midfielder")
    Goalkeeping_score = 50
    Defending_score = 30
    player_positions = {
        GoalkeeperPosition: Goalkeeping_score,
        DefencePosition:Defending_score
    }
    PlayerFirst = Player("Ali", player_positions)
    PlayerSecond = Player("Veli", player_positions)

    PlayerFirst.add_new_position(MidfieldPosition, 20)

    assert PlayerFirst.get_positions() == [GoalkeeperPosition, DefencePosition, MidfieldPosition]
    with pytest.raises(Exception) as e_info:
        PlayerSecond.add_new_position("FakePosition", 30)


test_adding_position_1()
test_adding_position_2()
test_updating_score_3()
test_updating_score_4()