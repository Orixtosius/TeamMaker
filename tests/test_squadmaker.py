import unittest
from src.players.football_player import FootballPlayer
from src.enums.positions import FootballPositions
from src.squadmaker import SquadMaker


class TestSqMaker(unittest.TestCase):

    player_5 = FootballPlayer("Veli", {FootballPositions.GOALKEEPER: 4})
    player_2 = FootballPlayer("Halim", {FootballPositions.GOALKEEPER: 3})
    player_1 = FootballPlayer("Ali", {FootballPositions.DEFENDER: 1})
    player_4 = FootballPlayer("Kaan", {FootballPositions.DEFENDER: 2})
    player_7 = FootballPlayer("Hakan", {FootballPositions.DEFENDER: 3})
    player_12 = FootballPlayer("Yusuf", {FootballPositions.DEFENDER: 4})
    player_6 = FootballPlayer("Arda", {FootballPositions.MIDFIELDER: 1})
    player_3 = FootballPlayer("Baran", {FootballPositions.MIDFIELDER: 2})
    player_8 = FootballPlayer("Enes", {FootballPositions.MIDFIELDER: 3})
    player_11 = FootballPlayer("Tarkan", {FootballPositions.MIDFIELDER: 4})
    player_9 = FootballPlayer("Cengiz", {FootballPositions.FORWARD: 3})
    player_10 = FootballPlayer("Mustafa", {FootballPositions.FORWARD: 4})
    player_13 = FootballPlayer("Mustafa", {FootballPositions.FORWARD: 4})
    player_14 = FootballPlayer("Mustafa", {FootballPositions.FORWARD: 4})

    positions = {
        FootballPositions.GOALKEEPER: 1, FootballPositions.DEFENDER: 2, 
        FootballPositions.MIDFIELDER: 2, FootballPositions.FORWARD: 1
    }
    
    all_player_bundle = [player_1, player_2, player_3, player_4, player_5, player_6,
                         player_7, player_8, player_9, player_10, player_11, player_12]
    
    asym_player_bundle = [player_1, player_2, player_3, player_4, player_5,
                         player_7, player_8, player_9, player_10, player_11, player_13, player_14]

    def test_empty_rooster(self):
        sq_maker = SquadMaker()
        self.assertEqual(sq_maker.players, None)

    def test_create_squadmaker(self):
        
        sq_maker = SquadMaker([self.player_1, self.player_2])
        self.assertEqual(sq_maker.players, [self.player_1, self.player_2])

    # def test_add_extra_positions(self):      
    #     sq_maker = SquadMaker([self.player_1])
    #     self.assertEqual(sq_maker.players, [self.player_1])    
    #     sq_maker.create_rooster(self.player_2, self.player_3)
    #     self.assertEqual(sq_maker.players, [self.player_1, self.player_2, self.player_3])

    # def test_gk_assignement(self):
    #     sq_maker = SquadMaker(self.all_player_bundle)
    #     sq_maker.players = sq_maker.players
    #     left_quota = sq_maker.assign_players_position_wise(FootballPositions.GOALKEEPER, 2)
    #     goalkeepers = sq_maker.assigned_players_for_position
    #     self.assertEqual(0, left_quota)
    #     for gk in goalkeepers:
    #         self.assertIsInstance(gk, FootballPlayer)
    #         self.assertIn(FootballPositions.GOALKEEPER, gk.positions)

    # def test_gk_deficient_assignement(self):
    #     sq_maker = SquadMaker(self.all_player_bundle)
    #     sq_maker.decoy_rooster = sq_maker.rooster
    #     left_quota = sq_maker.assign_players_position_wise(FootballPositions.GOALKEEPER, 3)
    #     self.assertEqual(1, left_quota)
    #     goalkeepers = sq_maker.assigned_players_for_position
    #     for gk in goalkeepers:
    #         self.assertIsInstance(gk, FootballPlayer)
    #         self.assertIn(FootballPositions.GOALKEEPER, gk.positions)

    # def test_gk_abundant_assignement(self):
    #     sq_maker = SquadMaker(self.all_player_bundle)
    #     sq_maker.decoy_rooster = sq_maker.rooster
    #     left_quota = sq_maker.assign_players_position_wise(FootballPositions.GOALKEEPER, 1)
    #     self.assertEqual(0, left_quota)
    #     goalkeepers = sq_maker.assigned_players_for_position
    #     for gk in goalkeepers:
    #         self.assertIsInstance(gk, FootballPlayer)
    #         self.assertIn(FootballPositions.GOALKEEPER, gk.positions)

    # def test_create_swapped_teams(self):
    #     sq_maker = SquadMaker(self.all_player_bundle)
    #     teams = sq_maker.create_teams(self.positions, 2)
    #     for team in teams.values():
    #         self.assertEqual(6, team.player_nbr)
    #         print(team)

    # def test_create_unevenswapped_teams(self):
    #     sq_maker = SquadMaker(self.asym_player_bundle)
    #     teams = sq_maker.create_teams(self.positions, 2)
    #     for team in teams.values():
    #         self.assertEqual(6, team.player_nbr)
    #         print(team)
