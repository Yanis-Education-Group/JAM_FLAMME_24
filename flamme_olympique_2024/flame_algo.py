import pygame
import os
import random

class FlameParticle:
    def __init__(self, x = 1920 // 2, y = 1080 // 2, r = 20000000000, alpha_layer = 2, alpha_glow_diff = 2) -> None:
        self.x = x
        self.y = y
        self.r = r
        self.prev_r = r
        self.alpha_layers = alpha_layer
        self.alpha_glow_diff = alpha_glow_diff
        max_surf = 2 * self.r * pow(self.alpha_layers, 2) * self.alpha_glow_diff
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
        max_surf_size = 2 * self.r * self.alpha_layers * self.alpha_layers * self.alpha_glow_diff
        self.surf = pygame.Surface((max_surf_size, max_surf_size), pygame.SRCALPHA)
        for i in range(self.alpha_layers, -1, -1):
            alpha = 255 - i * (255 // self.alpha_layers - 5)
            if alpha <= 0:
                alpha = 0
            radius = self.r * i * i * self.alpha_glow_diff
            if self.r == 4 or self.r == 3:
                r, g, b = (255, 0, 0)
            elif self.r == 2:
                r, g, b = (255, 150, 0)
            else:
                r, g, b = (50, 50, 50)
            # r, g, b = (0, 0, 255)  # uncomment this to make the flame blue
            color = (r, g, b, alpha)
            pygame.draw.circle(self.surf, color, (self.surf.get_width() // 2, self.surf.get_height() // 2), radius)
        screen.blit(self.surf, self.surf.get_rect(center=(self.x, self.y)))


class FlameObject:
    def __init__(self, x=1920 // 2, y=1080 // 2):
        self.x = x
        self.y = y
        self.flame_intensity = 2
        self.flame_particles = []
        for i in range(self.flame_intensity * 25):
            self.flame_particles.append(FlameParticle(self.x + random.randint(-5, 5), self.y, random.randint(1, 5)))

    def draw(self, screen: pygame.Surface):
        for i in self.flame_particles:
            if i.prev_r <= 0:
                self.flame_particles.remove(i)
                self.flame_particles.append(FlameParticle(self.x + random.randint(-5, 5), self.y, random.randint(1, 5)))
                del i
                continue
            i.update()
            i.draw(screen)
