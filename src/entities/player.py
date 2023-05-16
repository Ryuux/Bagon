import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(100, 100))
        self.velocity = pygame.Vector2(0, 0)
        self.gravity = pygame.Vector2(0, 0.5)
        self.jump_power = -10
        self.is_jumping = False

    def update(self, height):
        self.apply_gravity()
        self.rect.move_ip(self.velocity)

        if self.rect.y >= height - self.rect.height:
            self.rect.y = height - self.rect.height
            self.velocity.y = 0
            self.is_jumping = False

    def apply_gravity(self):
        self.velocity += self.gravity

    def jump(self):
        if not self.is_jumping:
            self.velocity.y += self.jump_power
            self.is_jumping = True
