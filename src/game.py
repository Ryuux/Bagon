import pygame 
from utils.constants import __CONFIG__

WIDTH = __CONFIG__['width']
HEIGHT = __CONFIG__['height']
FPS = __CONFIG__['fps']

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.running = True

        pygame.init()
        pygame.display.set_caption('Game')

    def quit(self):
        self.running = False

    def update(self):
        events = pygame.event.get()
        event_handlers = {
            pygame.QUIT: self.quit,
            pygame.KEYDOWN: lambda event: self.quit() if event.key == pygame.K_ESCAPE else None
        }
        for event in events:
            handler = event_handlers.get(event.type)
            if handler:
                handler(event)

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            self.update()
            clock.tick(FPS)
        
        pygame.quit()
