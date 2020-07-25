import pygame
import math


WIDTH = 750
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
COLOR = (255, 255, 255)


def main():
    pygame.init()
    pygame.display.init()
    pygame.display.set_caption("Fractal Tree")
    run = True
    while run:
        draw_fractal_tree(WIN, WIDTH // 2, HEIGHT, 90, 10)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            draw_fractal_tree(WIN, WIDTH // 2, HEIGHT, 90, 10)
            pygame.display.flip()

    pygame.quit()


def draw_fractal_tree(win, a, b, ang, deepness):

    if deepness:
        c = a + int(math.cos(math.radians(ang)) * deepness * 10.0)
        d = b - int(math.sin(math.radians(ang)) * deepness * 10.0)
        pygame.draw.line(win, COLOR, (a, b), (c, d), 1)
        draw_fractal_tree(win, c, d, ang - 25, deepness - 1)
        draw_fractal_tree(win, c, d, ang + 25, deepness - 1)


if __name__ == "__main__":
    main()
