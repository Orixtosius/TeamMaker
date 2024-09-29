import unittest
from src.players.football_player import FootballPlayer
from src.enums.positions import FootballPositions


class TestPlayers(unittest.TestCase):

    def test_adding_position_1(self):
        PlayerScore = 60
        PlayerFirst = FootballPlayer("Ali", {FootballPositions.FORWARD: PlayerScore})
        self.assertEqual(PlayerFirst.position_scores[FootballPositions.FORWARD], 60)

    def test_updating_score_1(self):
        player_score = 70
        score_change = 3
        PlayerFirst = FootballPlayer("Ali", {FootballPositions.GOALKEEPER: player_score})
        PlayerFirst.update_player_score(FootballPositions.GOALKEEPER, score_change)
        self.assertEqual(PlayerFirst.position_scores[FootballPositions.GOALKEEPER], player_score + score_change)

    def test_updating_score_3(self):
        player_score = 70
        score_change = - 3
        PlayerFirst = FootballPlayer("Ali", {FootballPositions.GOALKEEPER: player_score})
        PlayerFirst.update_player_score(FootballPositions.GOALKEEPER, score_change)
        self.assertEqual(PlayerFirst.position_scores[FootballPositions.GOALKEEPER], player_score + score_change)

    # def test_updating_score_4():
    #     PlayerPosition = Ensembler.get_position("Goalkeeper")
    #     PlayerScore = 2
    #     score_change = -3
    #     PlayerFirst = Player("Ali", {PlayerPosition: PlayerScore})
    #     PlayerFirst.update_player_score(PlayerPosition, score_change)
    #     assert PlayerFirst.position_scores[PlayerPosition] == 0

    def test_add_new_position_to_player(self):
        goalkeeping_score = 50
        defending_score = 30
        player_positions = {
            FootballPositions.GOALKEEPER: goalkeeping_score,
            FootballPositions.DEFENDER:defending_score
        }
        player = FootballPlayer("Ali", player_positions)
        player.add_new_position(FootballPositions.MIDFIELDER, 20)
        expected = [FootballPositions.GOALKEEPER, FootballPositions.DEFENDER, FootballPositions.MIDFIELDER]
        self.assertListEqual(player.get_positions(), expected)