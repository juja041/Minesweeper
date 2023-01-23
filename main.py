import pygame
import os

WIDTH, HEIGHT = 500,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 60
pygame.display.set_caption("Minesweeper")

UNCOVERED_SQUARE_IMG = pygame.image.load(r'C:\learn\local_stuff\miny\Minesweeper\Images\uncovered_square.png')
UNCOVERED_SQUARE = pygame.transform.scale(UNCOVERED_SQUARE_IMG, (50,50))
def draw_window():
    WIN.fill((255,255,255))
    
    for i in range(10):
        for a in range(10):
            WIN.blit(UNCOVERED_SQUARE, (50*i,50*a))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        draw_window()
    
    pygame.quit()

if __name__ == "__main__":
    main()
        
        