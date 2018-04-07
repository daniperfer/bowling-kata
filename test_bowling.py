import unittest
from bowling import Bowling


class TestClass(unittest.TestCase):
    def test_case_all_strikes(self):
        game = "XXXXXXXXXXXX"
        game_score = 10*30
        bowling_game = Bowling()
        total_score = bowling_game.evaluate(game)
        self.assertEqual(total_score, game_score)

    def test_case_extra_ball_after_spare_in_last_frame(self):
        game = "XXXXXXXXX1/5"
        game_score = 7*30 + 1*(10+10+1) + 1*(10+1+9) + 1*(1+9) + 5
        bowling_game = Bowling()
        total_score = bowling_game.evaluate(game)
        self.assertEqual(total_score, game_score)

    def test_case_strike_in_extra_ball_after_spare_in_last_frame(self):
        game = "XXXXXXXXX1/X"
        game_score = 7*30 + 1*(10+10+1) + 1*(10+1+9) + 1*(1+9) + 10
        bowling_game = Bowling()
        total_score = bowling_game.evaluate(game)
        self.assertEqual(total_score, game_score)

    def test_case_spare_in_extra_balls_after_strike_in_last_frame_version1(self):
        game = "XXXXXXXXXX1/"
        game_score = 8*30 + 1*(10+10+1) + 1*(10+1+9)
        bowling_game = Bowling()
        total_score = bowling_game.evaluate(game)
        self.assertEqual(total_score, game_score)

    def test_case_spare_in_extra_balls_after_strike_in_last_frame_version2(self):
        game = "XXXXXXXXXX19"
        game_score = 8*30 + 1*(10+10+1) + 1*(10+1+9)
        bowling_game = Bowling()
        total_score = bowling_game.evaluate(game)
        self.assertEqual(total_score, game_score)

    def test_case_spare_in_extra_balls_after_strike_in_last_frame_version3(self):
        game = "XXXXXXXXXX9/"
        game_score = 8*30 + 1*(10+10+9) + 1*(10+9+1)
        bowling_game = Bowling()
        total_score = bowling_game.evaluate(game)
        self.assertEqual(total_score, game_score)

    def test_case_spare_in_extra_balls_after_strike_in_last_frame_version4(self):
        game = "XXXXXXXXXX91"
        game_score = 8*30 + 1*(10+10+9) + 1*(10+9+1)
        bowling_game = Bowling()
        total_score = bowling_game.evaluate(game)
        self.assertEqual(total_score, game_score)

    def test_case_nine_pins_in_all_frames(self):
        game = "9-9-9-9-9-9-9-9-9-9-"
        game_score = 10*9
        bowling_game = Bowling()
        total_score = bowling_game.evaluate(game)
        self.assertEqual(total_score, game_score)

    def test_case_spare_before_last_frame(self):
        game = "9-9-9-9-9-9-9-9-9/9-"
        game_score = 8*9 + 1*(10+9) + 1*9
        bowling_game = Bowling()
        total_score = bowling_game.evaluate(game)
        self.assertEqual(total_score, game_score)

    def test_case_all_zeros(self):
        game = "--------------------"
        game_score = 0
        bowling_game = Bowling()
        total_score = bowling_game.evaluate(game)
        self.assertEqual(total_score, game_score)

    def test_case_150_points(self):
        game = "5/5/5/5/5/5/5/5/5/5/5"
        game_score = 10*15
        bowling_game = Bowling()
        total_score = bowling_game.evaluate(game)
        self.assertEqual(total_score, game_score)

    def test_case_all_strikes_in_single_frame(self):
        single_frame = "XXX"
        single_frame_score = 10 + 10 + 10
        bowling_game = Bowling()
        total_score = bowling_game.evaluate(single_frame)
        self.assertEqual(total_score, single_frame_score)

    def test_case_two_strikes_in_two_frames(self):
        single_frame = "X17X44"
        single_frame_score = 1*(10+1+7) + 1*(1+7) + 1*(10+4+4)
        bowling_game = Bowling()
        total_score = bowling_game.evaluate(single_frame)
        self.assertEqual(total_score, single_frame_score)


if __name__ == "__main__":
    unittest.main()
