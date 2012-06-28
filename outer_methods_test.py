import unittest
import ball_game


class PrimesTest(unittest.TestCase):

    def test_load_sprite(self):
        """Method testing creating/loading of sprites."""
        sprite = ball_game.load_sprite("ball.png")
        self.assertEqual('<Sprite sprite(in 0 groups)>', str(sprite))
        self.assertEqual("<class 'pygame.sprite.Sprite'>", str(type(sprite)))

    def test_sgn(self):
        """Method testing is method return correct sign."""
        self.assertEqual(-1.0, ball_game.sgn(-5))
        self.assertEqual(1.0, ball_game.sgn(0))
        self.assertEqual(1.0, ball_game.sgn(5))

    def test_read_scores(self):
        """Method testing can we read from nonexistent files."""
        self.assertRaises(IOError, ball_game.read_scores, '/no_file')

    def test_write_scores(self):
        """Method testing can we write from nonexistent files."""
        self.assertRaises(IOError, ball_game.write_scores, '/no_file', 5)

if __name__ == '__main__':
    unittest.main()
