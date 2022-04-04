import pygame
from pygame.locals import *

def drawBlock():
    surface.fill((50, 168, 82))
    surface.blit(block, (block_x,block_y))
    pygame.display.flip()

if __name__ == "__main__":
    pygame.init()

    icon = pygame.image.load("icon.png")  # Zapisanie ikony do zmiennej
    pygame.display.set_icon(icon)  # Ustawienie ikony okna gry
    pygame.display.set_caption("Snake Game")  # Tytuł okna gry
    surface = pygame.display.set_mode((1000, 750))  # Stworzenie planszy o wymiarach w [px]
    surface.fill((50, 168, 82))  # Wypełnienie planszy kolorem 

    block = pygame.image.load("block.png").convert()  # Zapisanie bloku do zmiennej
    block_x = 100
    block_y = 100
    surface.blit(block, (block_x,block_y))  # Ustawienie elementu na ekanie wg współrzędnych

    pygame.display.flip()  # Prawidłowe wyświetlenie planszy

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                
                # Kierowanie obiektem
                if event.key == K_w:
                    block_y -= 25
                    drawBlock()
                if event.key == K_s:
                    block_y += 25
                    drawBlock()
                if event.key == K_d:
                    block_x += 25
                    drawBlock()
                if event.key == K_a:
                    block_x -= 25
                    drawBlock()
            elif event.type == QUIT:
                running = False

