import pygame
import os
import random

pygame.init()

SCREEN_WIDTH = pygame.display.Info().current_w
SCREEN_HEIGHT = pygame.display.Info().current_h
FPS = 60

class FlameParticule:
    def __init__(self, x = SCREEN_WIDTH // 2, y = SCREEN_HEIGHT // 2, r = 5, alpha_layer = 2, alpha_glow_diff = 2) -> None:
        self.x = x
        self.y = y
        self.r = r
        self.prev_r = r
        self.alpha_layer = alpha_layer
        self.alpha_glow_diff = alpha_glow_diff
        max_surf = 2 * self.r * pow(self.alpha_layer, 2) * self.alpha_glow_diff
        self.surf = pygame.Surface((max_surf, max_surf), pygame.SRCALPHA)
        self.burn_rate = 0.1 * random.randint(1, 4)

    def update(self) -> None:
        self.y -= 7 - self.r 
        self.x += random.randint(-self.r, self.r)
        self.prev_r -= self.burn_rate
        self.r = int(self.prev_r)
        if self.r <= 0:
            self.r = 1

    def draw(self, screen: pygame.Surface) -> None:
        max_surf = 2 * self.r * pow(self.alpha_layer, 2) * self.alpha_glow_diff
        self.surf = pygame.Surface((max_surf, max_surf), pygame.SRCALPHA)
        for i in range(self.alpha_layer, -1, -1):
            alpha = 255 - (255 // self.alpha_layer - 5) * i
            if (alpha < 0):
                alpha = 0
            self.radius = self.r * pow(i, 2) * self.alpha_glow_diff
            pygame.draw.circle(self.surf, (0, 0, 255, alpha), (self.surf.get_width() // 2, self.surf.get_height() // 2), self.radius)
        screen.blit(self.surf, self.surf.get_rect(center = (self.x, self.y)))

class FlameObject():
    def __init__(self, x = SCREEN_WIDTH // 2, y = SCREEN_HEIGHT // 2):
        self.x = x
        self.y = y
        self.intensity = 0
        self.particules = []
        for _ in range(self.intensity * 25):
            self.particules.append(FlameParticule(self.x + random.randint(-5,5), self.y + random.randint(1,5)))

    def draw(self, screen: pygame.Surface):
        for part in self.particules:
            if part.prev_r <= 0:
                self.particules.remove(part)
                self.particules.append(FlameParticule(self.x + random.randint(-5,5), self.y + random.randint(1,5)))
                del part
                continue
            part.update()
            part.draw(screen)

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    flame = FlameObject()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((0, 0, 0))
        flame.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

main()