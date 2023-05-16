import pygame
from entities.player import Player
from utils.constants import __SCREEN__

WIDTH = __SCREEN__['width']
HEIGHT = __SCREEN__['height']
FPS = __SCREEN__['fps']

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Game')
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(50, 50)

    def quit(self):
        self.running = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                elif event.key == pygame.K_SPACE:
                    self.player.jump()

    def update(self):
        self.handle_events()
        self.player.update(HEIGHT)

    def render(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.player.image, self.player.rect)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.update()
            self.render()
            self.clock.tick(FPS)

        pygame.quit()
