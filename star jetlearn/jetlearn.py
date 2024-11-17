import pgzrun

import random

TITLE = "house fruit collector"

WIDTH = 800
HEIGHT = 800
center_x = WIDTH//2
center_y = HEIGHT//2
center = (center_x, center_y)
game_failed = False
game_complete = False
score = 1

level = 1
final_level = 50
'-----------------------------------------------------------------------------------------------------------------------------------------'
mango = Actor("mango")
blueberry = Actor("blueberry")
strawberry = Actor("strawberry")
house = Actor("houseee")
choicee = None
fruits = [mango, blueberry, strawberry]
actor_destroyed = False
'-----------------------------------------------------------------------------------------------------------------------------------------'
def draw():
    global choicee, game_failed, game_complete
    screen.clear()
    screen.fill(color = "pink")
    house.draw()
    if choicee:
        if not actor_destroyed:
            choicee.draw()
    if game_failed:
        screen.fill("black")
        message("Game Over!!", "try again soon!")
    elif game_complete:
        screen.fill("black")
        message("Game won!!", "good job!")

def on_mouse_down(pos):
    global choicee, score, actor_destroyed, level
    if house.collidepoint(pos):
        choice = random.randint(0,2)
        actor_destroyed = False
        choicee = fruits[choice]
        movechoicee()
    elif choicee.collidepoint(pos):
        screen.clear()
        actor_destroyed = True
        move()
        level += 1
    else:
        game_over()

def message(heading, text):
    screen.draw.text(heading, center = (center_x, (center_y - 15)), fontsize = 50, color = "pink")
    screen.draw.text(text, center = (center_x, (center_y + 15)), fontsize = 30, color = "pink")
def game_is_complete():
    global level, final_level, game_complete
    if level == final_level:
        game_complete = True

def move():
    house.x = random.randint(50,WIDTH-50)
    house.y = random.randint(50, WIDTH - 50)
    screen.clear()

def movechoicee():
    choicee.x = random.randint(50, WIDTH-50)
    choicee.y = random.randint(50, WIDTH-50)

def game_over():
    global game_failed
    game_failed = True
    
    
pgzrun.go()