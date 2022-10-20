#TEST MODE, IN PROGESS

# Stepan Yashin proudy made this game, It took a lot of effort, But I had finally converted it into 2 player mode. ENJOY!!! 
#10/15/22, In airplane, added player 1 && fox. :) ( From Sydney to Auckland.)
# WASD PLAYER 1
# ARROW KEYS PLAYER 2
# Z & M TO RESET POSITION OF FOX / HEDGEHOG IF NEEDED
# Version 3.1, Added if going out of map boundary, Going back into screen.
import pygame
from random import randint
import pgzrun
import time
x = 150
y = 150
WIDTH = 500
HEIGHT = 500
time_left = 60
player_1_score = 0 
player_2_score = 0
game_over = False
fox = Actor("fox")
fox.pos = 150, 150
fox.xe = 150
fox.ye = 150
hedgehog = Actor("hedgehog")
hedgehog.pos = 150, 150
hedgehog.xe = 150
hedgehog.ye = 150
coin = Actor("coin")
coin.pos = 100, 200
background = pygame.image.load(r'C:\Users\Evgeny\Desktop\Python\Code GAMES\coin collector\images/3_dall_E_images_in_1_500_504.png')


def draw():
    screen.blit(background, (0, 0))
    fox.draw()
    coin.draw()
    hedgehog.draw()
    screen.draw.text("fox: " + str(player_1_score), color="black", topleft=(10, 10))
    screen.draw.text("hedgehog: " + str(player_2_score), color="black", topleft=(10, 30))

    if game_over:
        screen.fill("#800080")
        if (player_1_score > player_2_score):
            screen.draw.text("FOX WINS, SCORE: " + str(player_1_score), color="orange", topleft=(10, 30))
        if (player_2_score > player_1_score):
            screen.draw.text("HEDGEHOG WINS, SCORE: " + str(player_2_score), color="orange", topleft=(10, 30))
        if (player_1_score == player_2_score):
            screen.draw.text("TIE!", color="orange", topleft=(10, 30))
            

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update():
    global player_1_score
    global player_2_score
    if keyboard.left:
        fox.x = fox.x - 10
        fox.xe = fox.xe   - 10
        collision_fox()
        collision_hedgehog()
    elif keyboard.right:
        fox.x = fox.x + 10
        fox.xe = fox.xe  + 10
        collision_fox()
        collision_hedgehog()
    elif keyboard.up:
        fox.y = fox.y - 10
        fox.ye = fox.ye  - 10
        collision_fox()
        collision_hedgehog()
    elif keyboard.down:
        fox.y = fox.y + 10
        fox.ye = fox.ye + 10
        collision_fox()
        collision_hedgehog()
    elif keyboard.m:
        fox.y = 150
        fox.x = 150

    if keyboard.a:
        hedgehog.x = hedgehog.x - 10
        hedgehog.xe = hedgehog.xe  - 10
        collision_fox()
        collision_hedgehog()
    elif keyboard.d:
        hedgehog.x = hedgehog.x + 10
        hedgehog.xe = hedgehog.xe  + 10
        collision_fox()
        collision_hedgehog()
    elif keyboard.w:
        hedgehog.y = hedgehog.y - 10
        hedgehog.ye = hedgehog.ye  - 10
        collision_fox()
        collision_hedgehog()
    elif keyboard.s:
        hedgehog.y = hedgehog.y + 10
        hedgehog.ye = hedgehog.ye  + 10
        collision_fox()
        collision_hedgehog()
    elif keyboard.z:
        hedgehog.y = 150
        hedgehog.x = 150

    coin_collected = fox.colliderect(coin)
    coin_collected2 = hedgehog.colliderect(coin)
    if coin_collected:
        player_1_score = player_1_score + 1
        place_coin()
    if coin_collected2:
        player_2_score = player_2_score + 1
        place_coin()    
    collision_fox()
    collision_hedgehog()



def collision_fox():
    if fox.xe | fox.ye > 600:
        fox.x = 150
        fox.y = 150
        fox.ye = 150
        fox.xe = 150

    if fox.xe | fox.ye < 0:
        fox.x = 150
        fox.y = 150
        fox.ye = 150
        fox.xe = 150

def collision_hedgehog():
    if hedgehog.xe | hedgehog.ye > 600:
        hedgehog.x = 150
        hedgehog.y = 150
        hedgehog.ye = 150
        hedgehog.xe = 150

    if hedgehog.xe | hedgehog.ye < 0:
        hedgehog.x = 150
        hedgehog.y = 150
        hedgehog.ye = 150
        hedgehog.xe = 150

clock.schedule(time_up, 60)
place_coin()
pgzrun.go()



