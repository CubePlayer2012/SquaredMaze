# Program in Python to create a Snake GameAdd commentMore actions

from tkinter import *
import random

# Initialising Dimensions of Game
WIDTH = 500
HEIGHT = 500
SPACE_SIZE = 40
SNAKE = "#00FF00"
WALL = "#FFFFFF"
FOOD = "#0000FF"
BACKGROUND = "#000000"

#window.after(SPEED, next_turn, snake, food)

# function to check snake's collision and position
def check_collisions(x, y):
    global walls

    if x < 0 or x >= WIDTH-SPACE_SIZE:
        return True
    elif y < 0 or y >= HEIGHT-SPACE_SIZE:
        return True

    for wall in walls:
        if x == wall[0] and y == wall[1]:
            return True

    return False

# Function to control everything
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,
                       canvas.winfo_height()/2,
                       font=('consolas', 70),
                       text="GAME OVER", fill="red",
                       tag="gameover")

def drawPlayer(position):
    canvas.create_rectangle(
        position[0],
        position[1],
        position[0] + SPACE_SIZE,
        position[1] + SPACE_SIZE,
        fill=SNAKE, tag="player")

def drawWall(position):
    canvas.create_rectangle(
        position[0],
        position[1],
        position[0] + SPACE_SIZE,
        position[1] + SPACE_SIZE,
        fill=WALL, tag="wall")

def drawGoal(position):
    canvas.create_rectangle(
        position[0],
        position[1],
        position[0] + SPACE_SIZE,
        position[1] + SPACE_SIZE,
        fill=FOOD, tag="goal")

def check_is_on_goal(x,y):
    global food

    if x == food[0] and y == food[1]:
        return True

    return False


def tick(move):
    global snake
    x, y = snake

    if move == "up":
        y -= SPACE_SIZE
    elif move == "down":
        y += SPACE_SIZE
    elif move == "left":
        x -= SPACE_SIZE
    elif move == "right":
        x += SPACE_SIZE

    if check_collisions(x,y):
        return

    canvas.delete("player")

    snake = [x,y]

    canvas.create_rectangle(
        x, y,
        x + SPACE_SIZE,
        y + SPACE_SIZE, fill=SNAKE, tags="player")


    if check_is_on_goal(x,y):
        game_over()

def motion(event):
    x, y = int(event.x/SPACE_SIZE), int(event.y/SPACE_SIZE)
    #print('{}, {}'.format(x, y))

    canvas.delete("p_wall")

    canvas.create_rectangle(
        x * SPACE_SIZE,
        y * SPACE_SIZE,
        x * SPACE_SIZE + SPACE_SIZE,
        y * SPACE_SIZE + SPACE_SIZE,
        fill="#444444", tag="p_wall")

def click_handler(event):
    global walls

    x, y = int(event.x / SPACE_SIZE), int(event.y / SPACE_SIZE)

    for wall in walls:
        if (x * SPACE_SIZE, y * SPACE_SIZE) == (wall[0], wall[1]):
            walls.remove(wall)
            canvas.delete("wall")
            for wall in walls:
                drawWall(wall)
            return

    canvas.create_rectangle(
        x * SPACE_SIZE,
        y * SPACE_SIZE,
        x * SPACE_SIZE + SPACE_SIZE,
        y * SPACE_SIZE + SPACE_SIZE,
        fill="#FFFFFF", tag="wall")

    walls.append((x * SPACE_SIZE, y * SPACE_SIZE))

# Giving title to the gaming window
window = Tk()
window.title("GFG Snake game ")

score = 0
direction = 'up'

# Display of Points Scored in Game

label = Label(window, text="Points:{}".format(score),
              font=('consolas', 20))
label.pack()

canvas = Canvas(window, bg=BACKGROUND, height=HEIGHT, width=WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>',
            lambda event: tick('left'))
window.bind('<Right>',
            lambda event: tick('right'))
window.bind('<Up>',
            lambda event: tick('up'))
window.bind('<Down>',
            lambda event: tick('down'))

window.bind('<Return>',
            lambda event: print(walls))

snake = [160, 440]
walls = []

food = [400, 0]

drawPlayer(snake)
for wall in walls:
    drawWall(wall)
drawGoal(food)

window.bind('<Motion>', motion)
window.bind("<Button-1>", click_handler)

window.mainloop()