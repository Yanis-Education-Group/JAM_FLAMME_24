#! /usr/bin/python3

import time
import pygame

def getCurrentDb():
    return 100

def startGame():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    score = 0
    currentMeat = 0
    quit = False
    start = time.time()
    scoreFont = pygame.font.SysFont(None, 24)
    gameOverFont = pygame.font.SysFont(None, 48)
    while (time.time() - start < 60) and quit == False:
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (125, 125, 125), pygame.Rect(30, 1000, 1860, 30))
        scoreUI = scoreFont.render("Score: " + str(score), True, (255, 255, 255))
        timeUI = scoreFont.render("Time Left: " + str(int(60 - (time.time() - start))), True, (255, 255, 255))
        screen.blit(scoreUI, (20, 20))
        screen.blit(timeUI, (1800, 20))
        currentMeat += (getCurrentDb() / 100)
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(30, 1000, (currentMeat / 100) * 1860, 30))
        if currentMeat >= 100:
            score += 1
            currentMeat = 0
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit = True
        pygame.display.update()
    screen.fill((0, 0, 0))
    gameOver = gameOverFont.render("Game Over!", True, (255, 255, 255))
    scoreUI = gameOverFont.render("Final Score: " + str(score), True, (255, 255, 255))
    screen.blit(gameOver, (920, 510))
    screen.blit(scoreUI, (884, 570))
    pygame.display.update()
    while quit == False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit = True
    pygame.quit()
    return score