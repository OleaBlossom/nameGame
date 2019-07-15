import unittest
from unittest.mock import patch
import nameGame


class TestNameGame(unittest.TestCase):

    def setUp(self):
        self.games = nameGame.load_games()

    def test_load(self):
        for i in range(len(self.games)):
            game = self.games[i]
            self.assertTrue(game.get("title"))

    def test_inputs(self):
        test_cases = [(4, "a", "The video game you should create is: The Legend of Game"),
                      (4, "f", "The video game you should create is: T\u00f8mb Warriors"),
                      (4, "hi", "The video game you should create is: Metal Revolution")]
        for test_case in test_cases:
            with patch('builtins.input', return_value=test_case[1]) as patched:
                result = nameGame.play_game(self.games[test_case[0]])
                self.assertEqual(result, "%s" % test_case[2])

if __name__ == "__main__":
    unittest.main()
