import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0,0)
        self.radius = radius

    def draw(self, screen):
        raise NotImplementedError("Base class")
    
    def update(self,dt):
        raise NotImplementedError("Base class")
    
    def collision(self, CircleShape):
        distance = self.position.distance_to(CircleShape.position)
        if distance <= (self.radius + CircleShape.radius):
            return True
        return False