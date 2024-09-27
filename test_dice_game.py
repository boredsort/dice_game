import unittest
import logging

from game import Game
from dice import Dice

# Task 1.2 Write unit tests
class TestGameRules(unittest.TestCase):

    logger = logging.getLogger('dicegame')
    game = Game(logger)

    def test_rule_double_six(self):
        self.assertEqual(self.game.double_six(6, 6), True)
        self.assertEqual(self.game.double_six(6, 1), False)
        self.assertEqual(self.game.double_six(1, 1), False)

    def test_rule_double_one(self):
        self.assertEqual(self.game.double_one(1, 1), True)
        self.assertEqual(self.game.double_one(5, 5), False)
        self.assertEqual(self.game.double_one(3, 1), False)

    def test_rule_one_or_six(self):
        self.assertEqual(self.game.one_or_six(6, 1), True)
        self.assertEqual(self.game.one_or_six(1, 6), True)
        self.assertEqual(self.game.one_or_six(6, 6), True)
        self.assertEqual(self.game.one_or_six(1, 1), True)
        self.assertEqual(self.game.one_or_six(5, 1), False)
        self.assertEqual(self.game.one_or_six(4, 6), False)
        self.assertEqual(self.game.one_or_six(3, 3), False)
        self.assertEqual(self.game.one_or_six(1, 0), False)

    def test_rule_dice_rolls_range(self):
        num_of_rolls = 1000
        rolls = [Dice.roll() for _ in range(num_of_rolls)]
        for roll in rolls:
            with self.subTest(roll=roll):
                self.assertTrue(1 <= roll <= 6, "Out of range")


class TestGame(unittest.TestCase):

    logger = logging.getLogger('dicegame')
    game = Game(logger)

    def test_game_start_should_return_results(self):
        result = self.game.start()

        self.assertIsInstance(result, list, "Result should be a list")
        

if __name__ == "__main__":
    unittest.main(verbosity=2)