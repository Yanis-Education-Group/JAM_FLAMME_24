import time
import pygame
from recup_mic import stream, use_mic, close_mic
from meat_cooking import create_sprite, change_sprite

def getCurrentDb():
    return 100

def gameLoop(screen: pygame.Surface, score: int, currentMeat: int, start: float, scoreFont: pygame.font.Font, cooking_meat: pygame.Surface, rect_cooking_meat: pygame.Rect):

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (125, 125, 125), pygame.Rect(30, 1000, 1860, 30))
    scoreUI = scoreFont.render("Score: " + str(score), True, (255, 255, 255))
    timeUI = scoreFont.render("Time Left: " + str(int(60 - (time.time() - start))), True, (255, 255, 255))
    screen.blit(scoreUI, (20, 20))
    screen.blit(timeUI, (1800, 20))
    if stream.is_active():
        if (use_mic() >= 130):
            currentMeat += (use_mic() / 50)
        elif (use_mic() >= 70):
            currentMeat += (use_mic() / 100)
        time.sleep(0.1)
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(30, 1000, (currentMeat / 100) * 1860, 30))
    if currentMeat >= 100:
        score += 1
        change_sprite(cooking_meat, "assets/diff_meat/cooked_beef/5acf297e-aee1-43ff-ae02-2cda59aca16f.png")
        while rect_cooking_meat.y <= 0:
            rect_cooking_meat.y -= 5
        rect_cooking_meat.y = 200
        change_sprite(cooking_meat, "assets/diff_meat/raw_beef/8730aceb-86a9-4f1e-8f68-c200794d7a06.png")
        currentMeat = 0
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
    pygame.display.update()


def endGameLoop(screen: pygame.Surface, score: int, gameOverFont: pygame.font.Font):

    screen.fill((0, 0, 0))
    gameOver = gameOverFont.render("Game Over!", True, (255, 255, 255))
    scoreUI = gameOverFont.render("Final Score: " + str(score), True, (255, 255, 255))
    screen.blit(gameOver, (920, 510))
    screen.blit(scoreUI, (884, 570))


def loadAssets():

    scoreFont = pygame.font.SysFont(None, 24)
    gameOverFont = pygame.font.SysFont(None, 48)
    stream.start_stream()

    cooking_meat, rect_cooking_meat = create_sprite("assets/diff_meat/raw_beef/8730aceb-86a9-4f1e-8f68-c200794d7a06.png", 200, 200);

    return scoreFont, gameOverFont, cooking_meat, rect_cooking_meat


def startGame() -> None:
    screen = pygame.display.set_mode((800, 600))
    score = 0
    currentMeat = 0
    timer = time.time()

    scoreFont, gameOverFont, cooking_meat, rect_cooking_meat = loadAssets() 

    while (time.time() - timer < 60):
        gameLoop(screen, score, currentMeat, timer, scoreFont, cooking_meat, rect_cooking_meat)

    endGameLoop(screen, score, gameOverFont)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    close_mic()
    pygame.quit()
