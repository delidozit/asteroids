import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SPEED, PLAYER_TURN_SPEED
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    # boot.dev copy paste for drawing triangle

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt



    def shoot(self, dt):
        shot_direction = pygame.Vector2(0, 1)
        shot_direction = shot_direction.rotate(-self.rotation)
        shot_velocity = shot_direction * PLAYER_SHOOT_SPEED
        new_shot = Shot(self.position.x, self.position.y, shot_velocity)
        return new_shot

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) # forward vector
        self.position += forward * PLAYER_SPEED * dt # position update
        

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)