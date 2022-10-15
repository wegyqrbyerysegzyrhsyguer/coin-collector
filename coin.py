# Stepan Yashin proudy made this game, It took a lot of effort, But I had finally converted it into 2 player mode. ENJOY!!! 
#10/15/22, In airplane, added player 1 && fox. :) ( From Sydney to Auckland.)


from random import randint
import pgzrun
WIDTH = 500
HEIGHT = 500
player_1_score = 0 
player_2_score = 0
game_over = False

fox = Actor("fox")
fox.pos = 100, 100
hedgehog = Actor("hedgehog")
hedgehog.pos = 150, 100
coin = Actor("coin")
coin.pos = 200, 200

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    hedgehog.draw()
    screen.draw.text("hedgehog: " + str(player_1_score), color="black", topleft=(10, 10))
    screen.draw.text("fox: " + str(player_2_score), color="black", topleft=(10, 30))

    if game_over:
        screen.fill("pink")
        screen.draw.text("hedgehog: " + str(player_1_score), topleft=(10, 10), fontsize=60)
        screen.draw.text("fox: " + str(player_2_score), topleft=(10, 10), fontsize=60)

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
    elif keyboard.right:
        fox.x = fox.x + 10
    elif keyboard.up:
        fox.y = fox.y - 10
    elif keyboard.down:
        fox.y = fox.y + 10

    if keyboard.a:
        hedgehog.x = hedgehog.x - 10
    elif keyboard.d:
        hedgehog.x = hedgehog.x + 10
    elif keyboard.w:
        hedgehog.y = hedgehog.y - 10
    elif keyboard.s:
        hedgehog.y = hedgehog.y + 10

    coin_collected = fox.colliderect(coin)
    coin_collected2 = hedgehog.colliderect(coin)
    if coin_collected:
        player_1_score = player_1_score + 1
        place_coin()
    if coin_collected2:
        player_2_score = player_2_score + 1
        place_coin()

clock.schedule(time_up, 60)
place_coin()
pgzrun.go()

# WR 2 PLAYER: 2880
# WR 1 PLAYER: 2400