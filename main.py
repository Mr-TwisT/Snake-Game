import pygame
from pygame.locals import *
import time
import random

SIZE = 50

class Apple:
		def __init__(self, parentScreen):
				self.parentScreen = parentScreen
				self.appleImage = pygame.image.load("apple.png")
				self.x = SIZE * 4
				self.y = SIZE * 7

		def draw(self):
				self.parentScreen.blit(self.appleImage, (self.x, self.y))
				pygame.display.flip()
		
		def move(self):
				self.x = random.randint(0,19)*SIZE
				self.y = random.randint(0,14)*SIZE

class Snake:
		def __init__(self, parentScreen, length=1):
				self.length = length
				self.parentScreen = parentScreen
				self.block = pygame.image.load("block.png")  # Zapisanie bloku do zmiennej
				self.x = [100] * length
				self.y = [100] * length
				self.direction = 'down'

		def draw(self):
				self.parentScreen.fill((50, 168, 82))
				for i in range(self.length):
						self.parentScreen.blit(self.block, (self.x[i], self.y[i]))  # Ustawienie elementu na ekanie wg współrzędnych
				pygame.display.flip()

		def moveUp(self):
				self.direction = 'up'

		def moveDown(self):
				self.direction = 'down'

		def moveRight(self):
				self.direction = 'right'

		def moveLeft(self):
				self.direction = 'left'

		def walk(self):
				for i in range(self.length-1,0,-1):
						self.x[i] = self.x[i-1]
						self.y[i] = self.y[i-1]

				if self.direction == "up":
						self.y[0] -= SIZE
				if self.direction == "down":
						self.y[0] += SIZE
				if self.direction == "right":
						self.x[0] += SIZE
				if self.direction == "left":
						self.x[0] -= SIZE
				
				self.draw()

class Game:
		def __init__(self):
				pygame.init()

				icon = pygame.image.load("icon.png")  # Zapisanie ikony do zmiennej
				pygame.display.set_icon(icon)  # Ustawienie ikony okna gry
				pygame.display.set_caption("Snake Game")  # Tytuł okna gry
				self.surface = pygame.display.set_mode((1000, 750))  # Stworzenie planszy o wymiarach w [px]
				self.surface.fill((50, 168, 82))  # Wypełnienie planszy kolorem

				self.snake = Snake(self.surface, 6)  # Stworzenie obiektu snake na podstawie klasy Snake
				self.snake.draw()

				self.apple = Apple(self.surface)  # Stworzenie obiektu apple na podstawie klasy Apple
				self.apple.draw()

		def isCollision(self, x_apple, y_apple, x_snake, y_snake):
				if x_snake == x_apple and y_snake == y_apple:
						return True
				return False

		def play(self):
				self.snake.walk()
				self.apple.draw()

				if self.isCollision(self.apple.x, self.apple.y, self.snake.x[0], self.snake.y[0]):
						self.apple.move()

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
						
						# Zrobienie żeby wąż sam się poruszał
						self.play()
						time.sleep(0.1)  # Uśpienie na 0.35s

if __name__ == "__main__":
		game = Game()
		game.run()

