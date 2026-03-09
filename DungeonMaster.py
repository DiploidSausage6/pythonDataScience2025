# this is a program to implement a dungeon explorer game.

Level_1 = [
    ["W","W","W","W","W","W","W","W"], # W= wall
    ["W",".",".",".","E",".","T","W"], # P=player
    ["W",".","W",".",".",".",".","W"], # E=enemy
    ["W",".",".",".","W",".",".","W"], # .=empty space
    ["W","W","W","W","W","W","W","W"]
]

class Player: # player code
    def __init__(self):
        self.health = 100
        self.attack = 10
        self.gold = 0
        self.x = 1
        self.y = 1

player = Player()

class Enemy: # enemy code
    def __init__(self, x, y):
        self.health = 30
        self.attack = 5
        self.x = x
        self.y = y

import turtle

# Screen setup
screen = turtle.Screen()
screen.title("Dungeon Master")
screen.bgcolor("black")

drawer = turtle.Turtle()
drawer.speed(0)
drawer.hideturtle()

TILE_SIZE = 40

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
  
def draw_level():
    drawer.clear()

    for row in range(len(Level_1)):
        for col in range(len(Level_1[row])):

            if row == player.y and col == player.x:
              tile = "P"
            else:
              tile = game_map[row][col]

            screen_x = col * TILE_SIZE - 160
            screen_y = 100 - row * TILE_SIZE

            if tile == "W":
                draw_tile(screen_x, screen_y, "gray")
            elif tile == ".":
                draw_tile(screen_x, screen_y, "darkgreen")
            elif tile == "T":
                draw_tile(screen_x, screen_y, "gold")
            elif tile == "E":
                draw_tile(screen_x, screen_y, "red")
            elif tile == "P":
                draw_tile(screen_x, screen_y, "blue")

def move_up(): # movement code
    new_y = player.y - 1

    if Level_1[new_y][player.x] != "W":
        player.y = new_y
        draw_level()

  def move_down():
    new_y = player.y + 1

    if game_map[new_y][player.x] != "W":
        player.y = new_y
        draw_level()

def move_left():
    new_x = player.x - 1

    if game_map[player.y][new_x] != "W":
        player.x = new_x
        draw_level()

def move_right():
    new_x = player.x + 1

    if game_map[player.y][new_x] != "W":
        player.x = new_x
        draw_level()

screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

draw_map()
screen.mainloop()
