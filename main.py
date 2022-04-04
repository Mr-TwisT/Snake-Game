import pygame
from pygame.locals import *

class Snake:
		def __init__(self, parentScreen):
				self.parentScreen = parentScreen
				self.block = pygame.image.load("block.png").convert()  # Zapisanie bloku do zmiennej
				self.x = 100
				self.y = 100

		def draw(self):
				self.parentScreen.fill((50, 168, 82))
				self.parentScreen.blit(self.block, (self.x,self.y))  # Ustawienie elementu na ekanie wg współrzędnych
				pygame.display.flip()

		def moveUp(self):
				self.y -= 50
				self.draw()

		def moveDown(self):
				self.y += 50
				self.draw()

		def moveRight(self):
				self.x += 50
				self.draw()

		def moveLeft(self):
				self.x -= 50
				self.draw()

class Game:
		def __init__(self):
				pygame.init()

				icon = pygame.image.load("icon.png")  # Zapisanie ikony do zmiennej
				pygame.display.set_icon(icon)  # Ustawienie ikony okna gry
				pygame.display.set_caption("Snake Game")  # Tytuł okna gry
				self.surface = pygame.display.set_mode((1000, 750))  # Stworzenie planszy o wymiarach w [px]
				self.surface.fill((50, 168, 82))  # Wypełnienie planszy kolorem

				self.snake = Snake(self.surface)  # Stworzenie obiektu snake na podstawie klasy Snake
				self.snake.draw()

		def run(self):
				running = True
				while running:
						for event in pygame.event.get():
								if event.type == KEYDOWN:
										if event.key == K_ESCAPE:
												running = False

											# Kierowanie obiektem
										if event.key == K_w:
												self.snake.moveUp()

										if event.key == K_s:
												self.snake.moveDown()

										if event.key == K_d:
												self.snake.moveRight()

										if event.key == K_a:
												self.snake.moveLeft()

								elif event.type == QUIT:
										running = False

if __name__ == "__main__":
		game = Game()
		game.run()

