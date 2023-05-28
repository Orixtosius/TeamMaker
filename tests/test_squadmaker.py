import unittest
from src.players import Player
from src.positions import Positions
from src.squadmaker import SquadMaker


class TestSqMaker(unittest.TestCase):

    player_5 = Player("Veli", {Positions.GOALKEEPER: 4})
    player_2 = Player("Halim", {Positions.GOALKEEPER: 3})
    player_1 = Player("Ali", {Positions.DEFENDER: 1})
    player_4 = Player("Kaan", {Positions.DEFENDER: 2})
    player_7 = Player("Hakan", {Positions.DEFENDER: 3})
    player_12 = Player("Yusuf", {Positions.DEFENDER: 4})
    player_6 = Player("Arda", {Positions.MIDFIELDER: 1})
    player_3 = Player("Baran", {Positions.MIDFIELDER: 2})
    player_8 = Player("Enes", {Positions.MIDFIELDER: 3})
    player_11 = Player("Tarkan", {Positions.MIDFIELDER: 4})
    player_9 = Player("Cengiz", {Positions.FORWARD: 3})
    player_10 = Player("Mustafa", {Positions.FORWARD: 4})

    player_13 = Player("Mustafa", {Positions.FORWARD: 4})
    player_14 = Player("Mustafa", {Positions.FORWARD: 4})

    positions = {Positions.GOALKEEPER: 1, Positions.DEFENDER: 2, Positions.MIDFIELDER: 2, Positions.FORWARD: 1}
    

    all_player_bundle = [player_1, player_2, player_3, player_4, player_5, player_6,
                         player_7, player_8, player_9, player_10, player_11, player_12]
    
    asym_player_bundle = [player_1, player_2, player_3, player_4, player_5,
                         player_7, player_8, player_9, player_10, player_11, player_13, player_14]

    def test_empty_rooster(self):
        sq_maker = SquadMaker()
        self.assertEqual(sq_maker.rooster, None)

    def test_create_squadmaker(self):
        
        sq_maker = SquadMaker([self.player_1, self.player_2])
        self.assertEqual(sq_maker.rooster, [self.player_1, self.player_2])

    def test_add_extra_positions(self):
        
        sq_maker = SquadMaker([self.player_1])
        self.assertEqual(sq_maker.rooster, [self.player_1])
        
        sq_maker.create_rooster(self.player_2, self.player_3)
        self.assertEqual(sq_maker.rooster, [self.player_1, self.player_2, self.player_3])

    def test_gk_assignement(self):
        sq_maker = SquadMaker(self.all_player_bundle)
        sq_maker.decoy_rooster = sq_maker.rooster
        sq_maker.total_team_score = 0
        left_quota = sq_maker.assign_players_position_wise(Positions.GOALKEEPER, 2)
        goalkeepers = sq_maker.assigned_players_for_position
        self.assertEqual(0, left_quota)
        for gk in goalkeepers:
            self.assertIsInstance(gk, Player)
            self.assertIn(Positions.GOALKEEPER, gk.positions)

    def test_gk_deficient_assignement(self):
        sq_maker = SquadMaker(self.all_player_bundle)
        sq_maker.decoy_rooster = sq_maker.rooster
        left_quota = sq_maker.assign_players_position_wise(Positions.GOALKEEPER, 3)
        self.assertEqual(1, left_quota)
        goalkeepers = sq_maker.assigned_players_for_position
        for gk in goalkeepers:
            self.assertIsInstance(gk, Player)
            self.assertIn(Positions.GOALKEEPER, gk.positions)

    def test_gk_abundant_assignement(self):
        sq_maker = SquadMaker(self.all_player_bundle)
        sq_maker.decoy_rooster = sq_maker.rooster
        left_quota = sq_maker.assign_players_position_wise(Positions.GOALKEEPER, 1)
        self.assertEqual(0, left_quota)
        goalkeepers = sq_maker.assigned_players_for_position
        for gk in goalkeepers:
            self.assertIsInstance(gk, Player)
            self.assertIn(Positions.GOALKEEPER, gk.positions)

    def test_create_swapped_teams(self):
        sq_maker = SquadMaker(self.all_player_bundle)
        teams = sq_maker.create_teams(self.positions, 2)
        for team in teams.values():
            self.assertEqual(6, team.player_nbr)
            print(team)

    def test_create_unevenswapped_teams(self):
        sq_maker = SquadMaker(self.asym_player_bundle)
        teams = sq_maker.create_teams(self.positions, 2)
        for team in teams.values():
            self.assertEqual(6, team.player_nbr)
            print(team)
