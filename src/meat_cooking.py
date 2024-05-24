import pygame

def create_sprite(image_path, x, y):
    sprite = pygame.image.load(image_path)
    sprite_rect = sprite.get_rect()
    sprite_rect.topleft = [x, y]
    sprite = pygame.transform.scale(sprite, (200, 200))
    return sprite, sprite_rect

def change_sprite (sprite, new_image_path, cooked):
    if cooked:
        sprite = pygame.image.load(new_image_path)
        sprite = pygame.transform.scale(sprite, (200, 200))
    return sprite

# def place_meat():
#     sprite, sprite_rec = create_sprite("assets/diff_meat/raw_beef/8730aceb-86a9-4f1e-8f68-c200794d7a06.png", 200, 200)
#     change_sprite(sprite, "assets/diff_meat/cooked_beef/5acf297e-aee1-43ff-ae02-2cda59aca16f.png")