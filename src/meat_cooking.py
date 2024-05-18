import pygame

def create_sprite(image_path, x, y):
    sprite = pygame.image.load(image_path)
    sprite_rect = sprite.get_rect()
    sprite_rect.topleft = [x, y]
    return sprite, sprite_rect

def change_sprite (sprite, new_image_path, cooked):
    if cooked:
        sprite = pygame.image.load(new_image_path)
    return sprite