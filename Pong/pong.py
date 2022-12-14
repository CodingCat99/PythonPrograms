from multiprocessing.connection import wait
from socket import timeout
from time import time
from turtle import Screen
import random
import pygame
import sys
rounds = 0


def ball_anim():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_reset()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


pygame.init()
clock = pygame.time.Clock()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 7


def ball_reset():
    global rounds
    rounds += 1
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))

def ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed


font = pygame.font.SysFont("Courier New", 24)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed = 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed = 0
            if event.key == pygame.K_UP:
                player_speed = 0
    text = font.render(str(rounds), True, green, blue)
    textRect = text.get_rect()
    textRect.center = (screen_width // 2, screen_height // 2)
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,
                       0), (screen_width/2, screen_height))
    screen.blit(text, textRect)
    player.y += player_speed
    ball_anim()
    if player.bottom >= screen_height:
        player.bottom = screen_height
    if player.top <= 0:
        player.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
    if opponent.top <= 0:
        opponent.top = 0
    ai()
    pygame.display.flip()
    clock.tick(60)
