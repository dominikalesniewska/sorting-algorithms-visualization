import pygame
from settings import *
from bubble_sort import *
from insertion_sort import *
from selection_sort import *


class Plot:
    def __init__(self, samples, sort_type):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.sort_type = sort_type

        if self.sort_type == "Bubble Sort":
            self.generator = bubble_sort(samples)
        elif self.sort_type == "Insertion Sort":
            self.generator = insertion_sort(samples)
        elif self.sort_type == "Selection Sort":
            self.generator = selection_sort(samples)

        self.sorted_list = None
        pygame.display.set_caption(sort_type)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False

            self.screen.fill(BACKGROUND_COLOR)
            pygame.draw.rect(
                self.screen,
                BORDER_COLOR,
                pygame.Rect(MARGIN, MARGIN, WIDTH - 2 * MARGIN, HEIGHT - 2 * MARGIN),
                1,
            )

            font = pygame.font.SysFont(FONT, 20)
            text = font.render(self.sort_type, False, FONT_COLOR)

            try:
                self.sorted_list = next(self.generator)
            except StopIteration:
                pass

            self.draw_column()
            self.screen.blit(text, (MARGIN + 5, HEIGHT - MARGIN - 25))
            pygame.display.update()
            self.clock.tick(FPS)

    def draw_column(self):
        for i in range(len(self.sorted_list)):
            column_width = (WIDTH - 2 * MARGIN - 2) / (2 * len(self.sorted_list) - 1)
            x = MARGIN + i * 2 * column_width
            y = MARGIN + 3
            w = column_width
            h = self.sorted_list[i] / max(self.sorted_list) * (HEIGHT - 2 * MARGIN - 10)

            pygame.draw.rect(self.screen, COLUMN_COLOR, pygame.Rect(x, y, w, h))
