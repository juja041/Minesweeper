import pygame
import os
import random
import bombs

WIDTH, HEIGHT = 500,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 10
pygame.display.set_caption("Minesweeper")

UNCOVERED_SQUARE_IMG = pygame.image.load(r'C:\learn\local_stuff\miny\Minesweeper\Images\uncovered_square.png')
UNCOVERED_SQUARE = pygame.transform.scale(UNCOVERED_SQUARE_IMG, (50,50))
MINE_IMAGE = pygame.image.load(r'C:\learn\local_stuff\miny\Minesweeper\Images\mina.png')
MINE = pygame.transform.scale(MINE_IMAGE, (50,50))

images = []
for i in range(9):
    images.append(pygame.transform.scale(pygame.image.load(f'C:\learn\local_stuff\miny\Minesweeper\Images\{i}.png'), (50,50)))

images.append(pygame.transform.scale(pygame.image.load(r'C:\learn\local_stuff\miny\Minesweeper\Images\bomb-at-clicked-block.png'), (50,50)))


positions_already_clicked=set()




coordinates_list = []
def draw_window():
    WIN.fill((255,255,255))
    
    for i in range(10):
        for a in range(10):
            coordinates_list.append((50*i,50*a))
            WIN.blit(UNCOVERED_SQUARE, (50*i,50*a))
    
    for i in positions_already_clicked:
        what = bombs.dict_adj_pos.get(i)
        if what is True:
            WIN.blit(images[9], i)
        else:
            WIN.blit(images[what], i)
    
    
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        mouse_position = pygame.mouse.get_pos()
        left_clicked = pygame.mouse.get_pressed()[0]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        if left_clicked:
            
            position_clicked = ((mouse_position[0]//50)*50, (mouse_position[1]//50)*50)
            print(position_clicked)
            positions_already_clicked.add(position_clicked)
        
        draw_window()
            
            

        
        
    
            
        #print(list_squares)
    
    pygame.quit()

if __name__ == "__main__":
    main()
        
        