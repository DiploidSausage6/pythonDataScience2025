# This is a program to implement a dungeon explorer game.

import turtle

# =========================
# GAME STATE
# =========================

game_running = True
current_level = 0

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
    ["W",".","E",".",".",".","E","W"],
    ["W",".","E",".","E",".",".","W"],
    ["W",".",".",".","E",".","D","W"],
    ["W","W","W","W","W","W","W","W"]
]

Level_3 = [
    ["W","W","W","W","W","W","W","W"],
    ["W",".","E",".",".",".","T","W"],
    ["W",".","W",".","W",".",".","W"],
    ["W",".",".",".","W",".","D","W"],
    ["W","W","W","W","W","W","W","W"]
]

Level_4 = [
    ["W","W","W","W","W","W","W","W"],
    ["W",".",".",".","E",".","T","W"],
    ["W",".",".",".",".","W",".","W"],
    ["W",".",".",".","W",".","D","W"],
    ["W","W","W","W","W","W","W","W"]
]

levels = [Level_1, Level_2, Level_3, Level_4]
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
# SCREEN SETUP
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
# DRAW TILE FUNCTION
# =========================

def draw_tile(x, y, color):

    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.color(color)
    drawer.begin_fill()

    for i in range(4):
        drawer.forward(TILE_SIZE)
        drawer.right(90)

    drawer.end_fill()


# =========================
# DRAW HUD FUNCTION
# =========================

def draw_hud():

    hud.clear()
    hud.goto(-150, 160)

    text = "Health: " + str(player.health)
    text = text + "    Gold: " + str(player.gold)
    text = text + "    Level: " + str(current_level + 1)

    hud.write(text, font=("Arial", 16, "normal"))

    hud.goto(-150, 140)
    hud.write("Use arrow keys to move.", font=("Arial", 14, "normal"))

    hud.goto(-150, 120)
    hud.write("Press 'r' to restart the game.", font=("Arial", 14, "normal"))

    hud.goto(-150, 100)
    hud.write("---------------------------", font=("Arial", 14, "normal"))

# =========================
# DRAW LEVEL FUNCTION
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
                draw_tile(screen_x, screen_y, "gray")
            if tile == ".":
                draw_tile(screen_x, screen_y, "darkgreen")
            if tile == "T":
                draw_tile(screen_x, screen_y, "gold")
            if tile == "E":
                draw_tile(screen_x, screen_y, "red")
            if tile == "P":
                draw_tile(screen_x, screen_y, "blue")
            if tile == "H":
                draw_tile(screen_x, screen_y, "pink")
            if tile == "D":
                draw_tile(screen_x, screen_y, "purple")

            # Extra blank line for verbosity
            drawer.penup()
            drawer.goto(drawer.xcor(), drawer.ycor())

    draw_hud()


# =========================
# TILE EVENTS FUNCTION
# =========================

def check_tile():

    global game_running

    tile = game_map[player.y][player.x]

    if tile == "T":
        player.gold = player.gold + 10
        game_map[player.y][player.x] = "."
        print("You found treasure!")

    if tile == "H":
        player.health = player.health + 20
        if player.health > 100:
            player.health = 100
        game_map[player.y][player.x] = "."
        print("You found a potion!")

    if tile == "E":
        player.health = player.health - 15
        if player.health < 0:
            player.health = 0
        print("An enemy attacked!")

        if player.health <= 0:
            game_running = False
            game_over()
            return

    if tile == "D":
        next_level()

    print("Checked tile at position:", player.x, player.y)
    print("Current Health:", player.health)
    print("Current Gold:", player.gold)
    print("-------------------------------")


# =========================
# NEXT LEVEL FUNCTION
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
    print("Moved to next level:", current_level + 1)


# =========================
# GAME OVER FUNCTION
# =========================

def game_over():

    drawer.clear()
    hud.clear()

    drawer.goto(-120, 0)
    drawer.color("white")
    drawer.write("GAME OVER", font=("Arial", 30, "bold"))

    print("GAME OVER")
    print("Reset the game by pressing 'r'")


# =========================
# WIN GAME FUNCTION
# =========================

def win_game():

    drawer.clear()
    hud.clear()

    drawer.goto(-140, 0)
    drawer.color("white")
    drawer.write("YOU WIN!", font=("Arial", 30, "bold"))

    print("YOU WIN!")
    print("Thanks for playing!")


# =========================
# MOVEMENT FUNCTIONS
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
# RESTART FUNCTION
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

    print("Game restarted")
    print("-------------------------------")


# =========================
# CONTROLS
# =========================

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(restart, "r")


# =========================
# START GAME
# =========================

draw_level()
screen.mainloop()
