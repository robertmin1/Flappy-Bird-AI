import unittest
from main import Bird, Pipe, Base

class TestFlappyBird(unittest.TestCase):
    def test_bird_jump(self):
        bird = Bird(230, 350)
        initial_y = bird.y
        bird.jump()
        self.assertEqual(bird.vel, -10.5)
        self.assertEqual(bird.tick_count, 0)
        self.assertEqual(bird.height, initial_y)

    def test_bird_move(self):
        bird = Bird(230, 350)
        bird.move()
        self.assertEqual(bird.tick_count, 1)

    def test_pipe_set_height(self):
        pipe = Pipe(100)
        pipe.set_height()
        self.assertGreaterEqual(pipe.height, 50)
        self.assertLessEqual(pipe.height, 450)

    def test_base_move(self):
        base = Base(730)
        initial_x1 = base.x1
        initial_x2 = base.x2
        base.move()
        self.assertEqual(base.x1, initial_x1 - base.VEL)
        self.assertEqual(base.x2, initial_x2 - base.VEL)

if __name__ == '__main__':
    unittest.main()
