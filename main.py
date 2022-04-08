import pygame
from pygame.locals import *
import time
import random

SIZE = 50
BACKGROUND_COLOR = (50, 168, 82)


class Apple:
    def __init__(self, parentScreen):
        self.parentScreen = parentScreen
        self.appleImage = pygame.image.load("./images/apple.png")
        self.x = SIZE * 4
        self.y = SIZE * 7

    def draw(self):
        self.parentScreen.blit(self.appleImage, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0, 19)*SIZE
        self.y = random.randint(0, 14)*SIZE


class Snake:
    def __init__(self, parentScreen, length=1):
        self.length = length
        self.parentScreen = parentScreen
        # Zapisanie bloku do zmiennej
        self.block = pygame.image.load("./images/block.png")
        self.x = [100] * length
        self.y = [100] * length
        self.direction = 'down'

    def increaseLength(self):
        self.length += 1
        self.x.append(24)  # Tutaj może być losowa wartość np.:123
        self.y.append(24)  # Tutaj może być losowa wartość np.:123

    def draw(self):
        for i in range(self.length):
            # Ustawienie elementu na ekanie wg współrzędnych
            self.parentScreen.blit(self.block, (self.x[i], self.y[i]))
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
        for i in range(self.length-1, 0, -1):
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

        # Zapisanie ikony do zmiennej
        icon = pygame.image.load("./images/icon.png")
        pygame.display.set_icon(icon)  # Ustawienie ikony okna gry
        pygame.display.set_caption("Snake Game")  # Tytuł okna gry

        pygame.mixer.init()  # Inicjalizacja funkcji muzycznych
        self.playMusic()

        # Stworzenie planszy o wymiarach w [px]
        self.surface = pygame.display.set_mode((1000, 750))
        # self.surface.fill(BACKGROUND_COLOR)  # Wypełnienie planszy kolorem

        # Stworzenie obiektu snake na podstawie klasy Snake
        self.snake = Snake(self.surface, 2)
        self.snake.draw()

        # Stworzenie obiektu apple na podstawie klasy Apple
        self.apple = Apple(self.surface)
        self.apple.draw()

    def isCollision(self, x_apple, y_apple, x_snake, y_snake):
        if x_snake == x_apple and y_snake == y_apple:
            return True
        return False

    def playMusic(self):
        pygame.mixer.music.load("./sounds/backgroundMusic.mp3")
        # "-1" jest po to żeby muzyka była zapętlona
        pygame.mixer.music.play(-1)

    def playSound(self, soundName):
        sound = pygame.mixer.Sound(f"./sounds/{soundName}.mp3")
        pygame.mixer.Sound.play(sound)

    def renderBackground(self):
        bg = pygame.image.load("./images/bgImage.jpg")
        self.surface.blit(bg, (0, 0))

    def play(self):
        self.renderBackground()
        self.snake.walk()
        self.apple.draw()
        self.displayScore()
        pygame.display.flip()

        # Wąż uderza w jabłko
        if self.isCollision(self.apple.x, self.apple.y, self.snake.x[0], self.snake.y[0]):
            self.playSound("dingSound")
            self.apple.move()
            self.snake.increaseLength()

        # Wąż uderza w siebie samego
        for i in range(1, self.snake.length):
            if self.isCollision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                self.playSound("hitSound")
                raise "Game Over!"

    def showGameOverScreen(self):
        self.renderBackground()
        font = pygame.font.SysFont("Calibri", 30)
        lineOne = font.render(
            f"Game is over! Your score is {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(lineOne, (300, 300))
        lineTwo = font.render(
            f"To play again press SPACE. To exit press ESC.", True, (255, 255, 255))
        self.surface.blit(lineTwo, (225, 350))
        pygame.display.flip()

        pygame.mixer.music.pause()  # Zapauzuj muzykę gdy jest game over

    def displayScore(self):
        font = pygame.font.SysFont("Calibri", 30)  # Używany font
        score = font.render(
            f"Score: {self.snake.length}", True, (250, 250, 250))
        # Blit trzeba użyć zawsze gdy chcemy wyświetlić coś na ekranie
        self.surface.blit(score, (850, 10))

    def reset(self):
        self.snake = Snake(self.surface, 2)
        self.apple = Apple(self.surface)

    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    # Tutaj co ma się dziać gdy chcemy zagrać od nowa
                    if event.key == K_SPACE:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
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

            try:
                if not pause:
                    self.play()
            except Exception as e:
                pause = True
                self.showGameOverScreen()
                self.reset()

            time.sleep(0.2)  # Uśpienie na X[s]


if __name__ == "__main__":
    game = Game()
    game.run()
