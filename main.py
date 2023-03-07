import pygame
import os
import random
import bombs
from bombs import bombicky
import time
pygame.font.init()


WIDTH, HEIGHT = 500,500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 15
pygame.display.set_caption("Minesweeper")

UNCOVERED_SQUARE_IMG = pygame.image.load(r'Minesweeper\Images\uncovered_square.png')
UNCOVERED_SQUARE = pygame.transform.scale(UNCOVERED_SQUARE_IMG, (50,50))
#MINE_IMAGE = pygame.image.load(r'C:\learn\local_stuff\miny\Minesweeper\Images\mina.png')
#MINE = pygame.transform.scale(MINE_IMAGE, (50,50))

Font = pygame.font.SysFont("comicsans", 30)
gameover = Font.render("YOU LOST, ENTER TO PLAY AGAIN", 1, (0,0,0))
win = Font.render("YOU WON, ENTER TO PLAY AGAIN", 1, (0,0,0))


images = []
for i in range(9):
    images.append(pygame.transform.scale(pygame.image.load(f'Minesweeper\Images\{i}.png'), (50,50)))

images.append(pygame.transform.scale(pygame.image.load(r'Minesweeper\Images\bomb-at-clicked-block.png'), (50,50)))
images.append(pygame.transform.scale(pygame.image.load(r'Minesweeper\Images\unclicked-bomb.png'), (50,50)))

positions_already_clicked=set()


""" def zero_helper(position):
    listt = []
    listek=[]
    neco = bombs.adjacent(position)
    for i in neco:
        if bombs.dict_adj_pos.get(i) == 0:
            WIN.blit(images[bombs.dict_adj_pos.get(i)], i)
            zero_helper(i)
        else:
            WIN.blit(images[bombs.dict_adj_pos.get(i)], i) """
            
    


coordinates_list = []
blited_stuff = set()
ez = True

def draw_window():
    WIN.fill((255,255,255))
    
    for i in range(10):
        for a in range(10):
            coordinates_list.append((50*i,50*a))
            WIN.blit(UNCOVERED_SQUARE, (50*i,50*a))
    
    for i in positions_already_clicked:
        what = bombs.dict_adj_pos.get(i)
        if what is True:
            
            for y in bombs.dict_adj_pos:
                if bombs.dict_adj_pos.get(y) is True:
                    WIN.blit(images[10],y)
                    blited_stuff.add(y)
                else:
                    WIN.blit(images[bombs.dict_adj_pos.get(y)], y)
                    blited_stuff.add(y)
            WIN.blit(images[9], i)
            blited_stuff.add(i)
            WIN.blit(gameover, (0,200))
            
            
            global ez
            ez = False
            global GGEZ
            GGEZ = True
            global winn
            winn = False
            
        
        elif what == 0:
            WIN.blit(images[0], i)
            blited_stuff.add(i)
            #zero_helper(i)
            listt=[]
            listek=[]
            blbost = [i]
            
            for a in bombs.adjacent(i):
                WIN.blit(images[bombs.dict_adj_pos.get(a)], a)
                blited_stuff.add(a)
                if bombs.dict_adj_pos.get(a) == 0:
                    for w in bombs.adjacent(a):
                        WIN.blit(images[bombs.dict_adj_pos.get(w)], w)
                        blited_stuff.add(w)
                        if bombs.dict_adj_pos.get(w) == 0:
                            for z in bombs.adjacent(w):
                                WIN.blit(images[bombs.dict_adj_pos.get(z)], z)
                                blited_stuff.add(z)
                                if bombs.dict_adj_pos.get(z) == 0:
                                    for u in bombs.adjacent(z):
                                        WIN.blit(images[bombs.dict_adj_pos.get(u)], u)
                                        blited_stuff.add(u)
                                        '''if bombs.dict_adj_pos.get(u) == 0:
                                            for l in bombs.adjacent(u):
                                                WIN.blit(images[bombs.dict_adj_pos.get(l)], l)
                                                blited_stuff.add(l)'''
                                    
            
            """ while True:
                for h in blbost:     
                    for a in bombs.adjacent((i[0]+(i[0]-h[0]),i[1]+(i[1]-h[1]))):
                        WIN.blit(images[bombs.dict_adj_pos.get(a)], a)
                        if bombs.dict_adj_pos.get(a) == 0:
                            listt.append(True)
                            listek.append(a)
                        else:
                            listt.append(False)
                    
                    if not any(listt):
                        break
                    blbost.clear()
                    for w in listek:
                        blbost.append(w)
                    listek.clear() """

                
                    
                    
                    
            
            
        else:
            WIN.blit(images[what], i)
            blited_stuff.add(i)
    
    coord_set = set(coordinates_list)
    diference = coord_set - blited_stuff
    dif = set()
    for i in diference:
        dif.add(bombs.dict_adj_pos[i])
    if len(dif) == 1 and list(dif)[0] is True:
        for y in bombs.dict_adj_pos:
            if bombs.dict_adj_pos.get(y) is True:
                WIN.blit(images[10],y)
            else:
                WIN.blit(images[bombs.dict_adj_pos.get(y)], y)
        
        GGEZ = True
        

        
    
        
        
    
    
    pygame.display.update()

def main():
    global positions_already_clicked
    positions_already_clicked=set()
    global blited_stuff
    blited_stuff = set()
    global coordinates_list
    coordinates_list = []
    global GGEZ
    GGEZ = False
    global winn
    winn=False
    bombicky()
    #positions_already_clicked = set()
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
        
        if GGEZ == True:    
            while True:
                
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key== pygame.K_RETURN:
                            main()
        
        '''if ENDOFGAME == True:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            main()'''
                    
            

        
        
    
            
        #print(list_squares)
    
    
    pygame.quit()

if __name__ == "__main__":
    main()
        


""" listt=[]
        listek=[]
        blbost = [i]
        while True:
            for h in blbost:     
                for a in bombs.adjacent((i[0]+(i[0]-h[0]),i[1]+(i[1]-h[1]))):
                    WIN.blit(images[bombs.dict_adj_pos.get(a)], a)
                    if bombs.dict_adj_pos.get(a) == 0:
                        listt.append(True)
                        listek.append(a)
                    else:
                        listt.append(False)
                
                if not any(listt):
                    break
                blbost.clear()
                for w in listek:
                    blbost.append(w)
                listek.clear() """
                    
                    
                
                #for h in listek:
                    #for w in bombs.adjacent(h)