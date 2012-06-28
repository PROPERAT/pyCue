import unittest
import ball_game


class PrimesTest(unittest.TestCase):

    def test_class_board(self):
        """Method testing the class Board which is controlled by player."""
        visual = ball_game.load_sprite("ball.png")
        board = ball_game.Board()
        self.assertEqual('<rect(0, 0, 61, 18)>', str(board.get_rect()))
        self.assertEqual('<Sprite sprite(in 0 groups)>',
                         str(board.get_visual()))
        board.set_limits(5, 10)
        self.assertEqual(5, board.left_limit)
        self.assertEqual(10, board.right_limit)

    def test_class_ball(self):
        """Method testing the class Ball which is controlled by game logic."""
        visual = ball_game.load_sprite("ball.png")
        ball = ball_game.Ball()
        self.assertEqual('<Sprite sprite(in 0 groups)>',
                         str(ball.get_visual()))
        ball.update_position(5, 10)
        self.assertEqual(5, ball.get_real_position()[0])
        self.assertEqual(10, ball.get_real_position()[1])

if __name__ == '__main__':
    unittest.main()
