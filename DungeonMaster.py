# This is a program to implement a dungeon explorer game.

import turtle

game_running = True

# =========================
# LEVELS
# =========================

Level_1 = [
["W","W","W","W","W","W","W","W"],
["W",".",".",".","E",".","T","W"],
["W",".","W",".",".",".",".","W"],
["W",".",".",".","W",".","D","W"],
["W","W","W","W","W","W","W","W"]
]

Level_2 = [
["W","W","W","W","W","W","W","W"],
["W",".",".",".","E",".","T","W"],
["W",".","W",".",".",".",".","W"],
["W",".",".",".","W",".","D","W"],
["W","W","W","W","W","W","W","W"]
]

levels = [Level_1, Level_2]
current_level = 0

game_map = levels[current_level]

# =========================
# PLAYER
# =========================

class Player:

    def __init__(self):
        self.health = 100
        self.gold = 0
        self.x = 1
        self.y = 1

player = Player()

# =========================
# SCREEN
# =========================

screen = turtle.Screen()
screen.title("Dungeon Explorer")
screen.bgcolor("black")

drawer = turtle.Turtle()
drawer.speed(0)
drawer.hideturtle()

hud = turtle.Turtle()
hud.hideturtle()
hud.color("white")
hud.penup()

TILE_SIZE = 40

# =========================
# DRAW TILE
# =========================

def draw_tile(x,y,color):

    drawer.penup()
    drawer.goto(x,y)
    drawer.pendown()

    drawer.color(color)
    drawer.begin_fill()

    for i in range(4):
        drawer.forward(TILE_SIZE)
        drawer.right(90)

    drawer.end_fill()

# =========================
# DRAW HUD
# =========================

def draw_hud():

    hud.clear()
    hud.goto(-150,160)

    text = "Health: " + str(player.health)
    text = text + "   Gold: " + str(player.gold)
    text = text + "   Level: " + str(current_level + 1)

    hud.write(text,font=("Arial",16,"normal"))

# =========================
# DRAW LEVEL
# =========================

def draw_level():

    drawer.clear()

    for row in range(len(game_map)):

        for col in range(len(game_map[row])):

            if row == player.y and col == player.x:
                tile = "P"
            else:
                tile = game_map[row][col]

            screen_x = col * TILE_SIZE - 160
            screen_y = 100 - row * TILE_SIZE

            if tile == "W":
                draw_tile(screen_x,screen_y,"gray")

            if tile == ".":
                draw_tile(screen_x,screen_y,"darkgreen")

            if tile == "T":
                draw_tile(screen_x,screen_y,"gold")

            if tile == "E":
                draw_tile(screen_x,screen_y,"red")

            if tile == "P":
                draw_tile(screen_x,screen_y,"blue")

            if tile == "H":
                draw_tile(screen_x,screen_y,"pink")

            if tile == "D":
                draw_tile(screen_x,screen_y,"purple")

    draw_hud()

# =========================
# TILE EVENTS
# =========================

def check_tile():

    global game_running
    
    tile = game_map[player.y][player.x]

    if tile == "T":

        player.gold = player.gold + 10
        game_map[player.y][player.x] = "."
        print("You found treasure!")

    if tile == "H":
    player.health += 20
    if player.health > 100:
        player.health = 100
    game_map[player.y][player.x] = "."
    print("You found a potion!")
    
   if tile == "E":
    player.health -= 15
    if player.health < 0:
        player.health = 0
    print("An enemy attacked!")

    if player.health <= 0:
        game_running = False
        game_over()
        return
    if tile == "D":

        next_level()

# =========================
# NEXT LEVEL
# =========================

def next_level():

    global current_level
    global game_map

    current_level = current_level + 1

    if current_level >= len(levels):
        win_game()
        return

    game_map = levels[current_level]

    player.x = 1
    player.y = 1

    draw_level()

# =========================
# GAME OVER
# =========================

def game_over():

    drawer.clear()
    hud.clear()

    drawer.goto(-120,0)
    drawer.color("white")

    drawer.write("GAME OVER",
    font=("Arial",30,"bold"))

# =========================
# WIN GAME
# =========================

def win_game():

    drawer.clear()
    hud.clear()

    drawer.goto(-140,0)
    drawer.color("white")

    drawer.write("YOU WIN!",
    font=("Arial",30,"bold"))

# =========================
# MOVEMENT
# =========================

def move_up():

    if not game_running:
        return

    new_y = player.y - 1

    if game_map[new_y][player.x] != "W":
        player.y = new_y
        check_tile()
        if game_running:
            draw_level()
            
def move_down():
    
    if not game_running:
        return

    new_y = player.y + 1
    if game_map[new_y][player.x] != "W":
        player.y = new_y
        check_tile()
        if game_running:
            draw_level()

def move_left():

    if not game_running:
        return
        
    new_x = player.x - 1

    if game_map[player.y][new_x] != "W":
        player.x = new_x
        check_tile()
        
        if game_running:
            draw_level()
        
def move_right():
    
    if not game_running:
        return

    new_x = player.x + 1

    if game_map[player.y][new_x] != "W":
        player.x = new_x
        check_tile()
        
        if game_running:
            draw_level()

# =========================
# RESTART GAME
# =========================

def restart():

    global current_level
    global game_map
    global game_running

    game_running = True
    
    player.health = 100
    player.gold = 0

    player.x = 1
    player.y = 1

    current_level = 0
    game_map = levels[current_level]

    draw_level()

# =========================
# CONTROLS
# =========================

screen.listen()

screen.onkey(move_up,"Up")
screen.onkey(move_down,"Down")
screen.onkey(move_left,"Left")
screen.onkey(move_right,"Right")

screen.onkey(restart,"r")

# =========================
# START GAME
# =========================

draw_level()

screen.mainloop()
