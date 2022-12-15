import pygame
from settings import *
from bubble_sort import *
import random

class Plot:
    def __init__(self,samples):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        self.generator = bubble_sort(samples)
        self.sorted_list = None
        pygame.display.set_caption(CAPTION)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
            
            self.screen.fill(BACKGROUND_COLOR)
            pygame.draw.rect(self.screen,BORDER_COLOR,pygame.Rect(MARGIN,MARGIN,WIDTH-2*MARGIN,HEIGHT-2*MARGIN),1)

            font = pygame.font.SysFont(FONT, 20)
            text = font.render('Bubble sort',False,FONT_COLOR)

            try:
                self.sorted_list = next(self.generator)
            except StopIteration:
                pass

            self.draw_column()
            self.screen.blit(text,(MARGIN+5,HEIGHT-MARGIN-25))
            pygame.display.update()
            self.clock.tick(FPS)

    def draw_column(self):
        for i in range(len(self.sorted_list)):
            column_width = (WIDTH-2*MARGIN-2)/(2*len(self.sorted_list)-1)
            x = MARGIN+i*2*column_width
            y = MARGIN+3
            w = column_width
            h = self.sorted_list[i]/max(self.sorted_list)*(HEIGHT-2*MARGIN-10)

            pygame.draw.rect(self.screen,COLUMN_COLOR,pygame.Rect(x,y,w,h))

if __name__ == "__main__":
    samples = random.sample(range(0, 100), 100)
    plot = Plot(samples)
    plot.run()