import pygame
import random
import math
import datetime
import pickle


def load_sprite(name):
    """Method gets image's name and return sprite."""
    result = pygame.sprite.Sprite()
    image = pygame.image.load(name)
    result.image = image
    result.rect = pygame.rect.Rect((0.0, 0.0), image.get_size())
    return result


def read_scores(filename):
    res = ''
    with open(filename, 'rb') as file:
        res += pickle.load(file)
    return res


def write_scores(filename, scores):
    """Method write datatime and scores in file."""
    curr_scores = read_scores(filename)
    now_datetime = str(datetime.datetime.now())
    res = '{0}\nDate({1}): {2} scores'.format(curr_scores,
                                              now_datetime, scores)
    with open(filename, 'wb') as file:
        pickle.dump(res, file)


def sgn(arg):
    """Return sign of the argument 'arg'."""
    if arg < 0:
        return -1.0
    else:
        return 1.0


class Board():

    def __init__(self):
        """Create player's board as image."""
        self.visual = load_sprite("player.jpg")
        self.left_limit = 0
        self.right_limit = 0

    def get_rect(self):
        return self.visual.rect

    def update_position(self, x, y):
        """Will move the rectangle with offsets x and y."""
        if (self.visual.rect.left + x >= self.left_limit and
                self.visual.rect.right + x <= self.right_limit):
            self.visual.rect = self.visual.rect.move(x, y)

    def get_visual(self):
        return self.visual

    def set_limits(self, left, right):
        self.left_limit = left
        self.right_limit = right


class Ball():

    def __init__(self):
        """Create ball as image."""
        self.visual = load_sprite("ball.png")

        """Set x, y center coordinates and radius of ball."""
        self.radius = self.visual.rect.width // 2
        self.position_x = 0
        self.position_y = 0

        """Set x, y velocity"""
        self.velocity_x = 0
        self.velocity_y = 0

    def set_position(self, x, y):
        self.position_x = 0
        self.position_y = 0

    def update_position(self, x, y):
        """Will move the rectangle with offsets x and y."""
        self.visual.rect = self.visual.rect.move(x, y)
        self.position_x += x
        self.position_y += y

    def get_visual(self):
        return self.visual

    def get_real_position(self):
        return (self.position_x, self.position_y, self.radius)


class Walls():

    def __init__(self):
        """
            Create four walls: (left, rigth, top, bottom)
            as coordinate system: (Ox, Ox, Oy, Oy).
        """
        self.walls = (0, 640, 0, 480)

    def get_walls(self):
        return self.walls


class Game(object):

    def main(self, screen):
        """Main method displayed window and draw."""
        pygame.display.set_caption("Ball Game")
        clock = pygame.time.Clock()
        background = pygame.image.load('Background.jpg')
        self.sprites = pygame.sprite.Group()

        """Create ball, board and walls."""
        self.ball = Ball()
        self.board = Board()
        self.walls = Walls()

        # self.ball.update_position(320,240)
        # self.ball.velocity_x = -150
        # self.ball.velocity_y = 150

        self.board.set_limits(0, 640)
        self.board.update_position(0, 462)

        self.sprites.add(self.ball.get_visual())
        self.sprites.add(self.board.get_visual())

        self.player_ball_hits_counter = 0

        """Infinity drawing loop."""
        self.running = True
        self.is_main_menu = True
        self.is_game_over_menu = False
        while self.running:
            dt = clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            elapsed = dt
            while elapsed > 0:
                update_time = 0
                if elapsed > 35:
                    update_time = 35
                    elapsed -= 35
                else:
                    update_time = elapsed
                    elapsed = 0
                self.update_elements(update_time / 1000.0)

            screen.blit(background, (0, 0))
            self.sprites.draw(screen)
            if self.is_main_menu:
                # screen.blit(background, (0, 0))
                self.main_menu()
                self.sprites.draw(screen)
            elif self.is_game_over_menu:
                # screen.blit(background, (0, 0))
                self.game_over_menu()
                self.sprites.draw(screen)
            else:
                # screen.blit(background, (0, 0))
                self.sprites.draw(screen)
            pygame.display.flip()

    def update_elements(self, dt):
        """Update drawing of ball and board."""

        """Movement of board."""
        key = pygame.key.get_pressed()
        distance_for_board = 0
        if key[pygame.K_LEFT]:
            distance_for_board -= 300 * dt
        if key[pygame.K_RIGHT]:
            distance_for_board += 300 * dt

        self.board.update_position(distance_for_board, 0)

        delta_x = dt * self.ball.velocity_x
        delta_y = dt * self.ball.velocity_y

        """ball_coord: x, y, r"""
        ball_coord = self.ball.get_real_position()

        """If ball hit left or right wall."""
        if ((delta_x + ball_coord[0]) + ball_coord[2]
                <= self.walls.get_walls()[0]
                or self.walls.get_walls()[1]
                    <= (delta_x + ball_coord[0]) + ball_coord[2]):
            self.ball.velocity_x = - self.ball.velocity_x

        """If ball hit top wall."""
        if ((delta_y + ball_coord[1]) + ball_coord[2]
                <= self.walls.get_walls()[2]):
            self.ball.velocity_y = - self.ball.velocity_y

        """If ball hit the board."""
        if self.is_ball_hits_board(ball_coord, delta_x, delta_y):
            self.ball.velocity_y = - self.ball.velocity_y
            self.player_ball_hits_counter += 1

        """If ball hit the bottom."""
        if ((delta_y + ball_coord[1]) + ball_coord[2]
                >= self.walls.get_walls()[3]):
            self.ball.update_position(320, 240)
            self.ball.velocity_x = 0
            self.ball.velocity_y = 0
            self.is_game_over_menu = True

        self.ball.update_position(delta_x, delta_y)

        """Every 10th hit goes to next level => faster ball."""
        if (self.player_ball_hits_counter % 10 == 0
                and self.player_ball_hits_counter > 0):
            self.ball.velocity_x += 10
            self.ball.velocity_y += 10

    def is_ball_hits_board(self, ball_coord, delta_x, delta_y):
        """
            Get ball coordinates and x, y movement distinctions
            and calculated if ball hits the board - returns True
            and if ball doesn't hit the board - returns False.
        """
        ball_x = delta_x + ball_coord[0]
        ball_y = delta_y + ball_coord[1]
        ball_r = ball_coord[2]

        x1 = self.board.get_rect().left - ball_x
        x2 = self.board.get_rect().right - ball_x

        y1 = self.board.get_rect().top - ball_y
        y2 = self.board.get_rect().top - ball_y

        dx = float(x2 - x1)
        dy = float(y2 - y1)
        dr = math.sqrt(dx ** 2 + dy ** 2)
        D = float(x1 * y2 - x2 * y1)

        discriminant = (ball_r ** 2) * (dr ** 2) - D ** 2

        if discriminant < 0:
            return False
        x_intersect_1 = (((D * dy) - dx * sgn(dy) * math.sqrt(discriminant))
                        / dr ** 2)
        x_intersect_2 = (((D * dy) + dx * sgn(dy) * math.sqrt(discriminant))
                        / dr ** 2)

        if ((x1 <= x_intersect_1 and x_intersect_1 <= x2)
                or (x1 <= x_intersect_2 and x_intersect_2 <= x2)):
            return True
        else:
            return False

    def main_menu(self):
        """Display Main Menu text."""
        menu_font = pygame.font.SysFont("Comic Sans MS", 50)
        label_new_game = menu_font.render("New Game - F1", 1, (255, 255, 0))
        screen.blit(label_new_game,
                    (320 - label_new_game.get_width() // 2, 170))

        label_load_game = menu_font.render("Quit Game - ESC", 1, (255, 255, 0))
        screen.blit(label_load_game,
                    (320 - label_load_game.get_width() // 2, 230))

        """Main Menu functionality."""
        key = pygame.key.get_pressed()
        if key[pygame.K_F1]:
            self.is_main_menu = False
            self.is_game_over_menu = False
            self.playing = True
            self.ball.set_position(0, 0)
            self.ball.update_position(320, 240)
            self.ball.velocity_x = - 150
            self.ball.velocity_y = 150
            self.player_ball_hits_counter = 0
        if key[pygame.K_ESCAPE]:
            self.running = False
            self.is_main_menu = False

    def game_over_menu(self):
        """Display Game Over Menu text."""
        menu_font = pygame.font.SysFont("Comic Sans MS", 55)
        label_new_game = menu_font.render("Game Over!", 1, (255, 255, 0))
        screen.blit(label_new_game,
                    (320 - label_new_game.get_width() // 2, 170))

        menu_font = pygame.font.SysFont("Comic Sans MS", 20)
        label_load_game = menu_font.render("To open Main Menu press 'Enter'.",
                                           1, (255, 255, 0))
        screen.blit(label_load_game,
                    (320 - label_load_game.get_width() // 2, 230))

        pygame.display.flip()

        """Playing music and open Main Menu functionality."""
        pygame.mixer.music.load('game_over.mp3')
        if self.playing:
            pygame.mixer.music.play()
            pygame.mixer.music.fadeout(3000)
            self.playing = False
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            pygame.mixer.music.stop()
            self.is_game_over_menu = False
            self.is_main_menu = True
            write_scores('scores.txt', self.player_ball_hits_counter)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    Game().main(screen)
