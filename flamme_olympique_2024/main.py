import time
import pygame
from recup_mic import stream, use_mic, close_mic
from meat_cooking import create_sprite, change_sprite
from flame_algo import FlameObject

def startGame() -> None:
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    timer = time.time()

    scoreFont = pygame.font.SysFont(None, 24)
    gameOverFont = pygame.font.SysFont(None, 48)
    stream.start_stream()

    cooking_meat, rect_cooking_meat = create_sprite("assets/diff_meat/raw_beef/8730aceb-86a9-4f1e-8f68-c200794d7a06.png", 200, 200);
    cauldron, cauldron_rect = create_sprite("assets/cauldron.png", 200, 200)
    olymp, olymp_rect = create_sprite("assets/olympic_rings.png", 100, 100)

    score = 0
    currentMeat = 0
    flame = FlameObject()

    while (time.time() - timer < 60):
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (125, 125, 125), pygame.Rect(30, 1000, 1860, 30))
        scoreUI = scoreFont.render("Score: " + str(score), True, (255, 255, 255))
        timeUI = scoreFont.render("Time Left: " + str(int(60 - (time.time() - timer))), True, (255, 255, 255))
        screen.blit(cooking_meat, (860, 200))
        screen.blit(scoreUI, (20, 20))
        screen.blit(timeUI, (1800, 20))
        screen.blit(cauldron, (860, 555))
        screen.blit(olymp, (910, 565))
        if stream.is_active():
            if (use_mic() >= 130):
                currentMeat += (use_mic() / 50)
            elif (use_mic() >= 70):
                currentMeat += (use_mic() / 100)
            time.sleep(0.1)
        flame.draw(screen)
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(30, 1000, (currentMeat / 100) * 1860, 30))
        if currentMeat >= 100:
            score += 1
            cooking_meat = change_sprite(cooking_meat, "assets/diff_meat/cooked_beef/5acf297e-aee1-43ff-ae02-2cda59aca16f.png")
            x = 860
            while x >= -250:
                x -= 5
                screen.blit(cooking_meat, (x, 200))
                pygame.display.update()
            rect_cooking_meat.y = 200
            cooking_meat = change_sprite(cooking_meat, "assets/diff_meat/raw_beef/8730aceb-86a9-4f1e-8f68-c200794d7a06.png")
            currentMeat = 0
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        pygame.display.update()

    screen.fill((0, 0, 0))
    gameOver = gameOverFont.render("Game Over!", True, (255, 255, 255))
    scoreUI = gameOverFont.render("Final Score: " + str(score), True, (255, 255, 255))
    screen.blit(gameOver, (920, 510))
    screen.blit(scoreUI, (884, 570))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    close_mic()
    pygame.quit()
