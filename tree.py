import pygame
import math
import time

WIDTH = 750
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
COLOR = (255, 255, 255)
INIT_LENGTH = 200
RBRANCH_ANGLE = math.pi / 4
LBRANCH_ANGLE = math.pi - math.pi / 4


def main():
    pygame.init()
    pygame.display.init()
    pygame.display.set_caption("Fractal Tree")
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            draw_fractal_tree(WIN, WIDTH // 2, HEIGHT, -90, 10)
            pygame.display.flip()

    pygame.quit()


def draw_fractal_tree(win, a, b, pos, deepness):

    if deepness:
        c = a + int(math.cos(math.radians(pos)) * deepness * 10.0)
        d = b + int(math.sin(math.radians(pos)) * deepness * 10.0)
        pygame.draw.line(win, COLOR, (a, b), (c, d), 1)
        draw_fractal_tree(win, c, d, pos - 25, deepness - 1)
        draw_fractal_tree(win, c, d, pos + 25, deepness - 1)


if __name__ == "__main__":
    main()
