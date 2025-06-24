# Program in Python to create a Snake GameAdd commentMore actions
from time import sleep
from tkinter import *
import random
global lv2
# Initialising Dimensions of Game
WIDTH = 500
HEIGHT = 500
SPACE_SIZE = 40
SNAKE = "#00FF00"
WALL = "#FFFFFF"
FOOD = "#0000FF"
BACKGROUND = "#000000"
PONTOS = 0
current_level = 1

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
def lvStart(level_number, pontos, playB, player_pos, food_pos):
    global current_level, snake, walls, score, food
    current_level = level_number
    canvas.delete(ALL)
    snake = player_pos
    walls = levels[level_number]['walls']
    score += 1
    food = food_pos
    label.config(text=pontos)
    drawPlayer(snake)
    for w in walls: drawWall(w)
    drawGoal(food)
    playB.destroy()

def game_over(placeBPlay, lv):
    canvas.delete(ALL)
    canvas.create_text(
        canvas.winfo_width()/2,
        canvas.winfo_height()/2,
        font=('consolas', 70),
        text=f"LEVEL {lv}",
        fill="green",
        tag="gameover"
    )
    placeBPlay.place(width=200, height=100, x=150, y=350)

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
        if check_is_on_goal(x, y):
            # em vez de sempre lv2, usa current_level+1
            next_lvl = current_level + 1
            btn = levels.get(next_lvl, {}).get('button')
            if btn:
                game_over(btn, next_lvl)
            else:
                # acabou
                canvas.delete(ALL)
                canvas.create_text(
                    canvas.winfo_width() / 2,
                    canvas.winfo_height() / 2,
                    text="Parabéns,\n terminaste!",
                    font=('consolas', 40),
                    fill="yellow")
                label.config(text='Pontos: 5')

def inicio():
    global menuTitulo, play
    play.destroy()
    menuTitulo.destroy()
    drawPlayer(snake)
    for wall in walls:
        drawWall(wall)
    drawGoal(food)

# Giving title to the gaming window
window = Tk()
window.title("Squared Maze")



canvas = Canvas(window, bg=BACKGROUND, height=HEIGHT, width=WIDTH)
canvas.pack()
score = 0
direction = 'up'



# Display of Points Scored in Game
menuTitulo = Label(window, text='Squared Maze', bg=BACKGROUND, fg='blue', font=("Arial", 50))
menuTitulo.place(height=60, width=500, x=2, y=70)

play = Button(window, bg=SNAKE, text="", command=inicio)
play.place(width=100, height=100, x=200,  y=250)

label = Label(window, text="Points: 0".format(score),
              font=('consolas', 20))
label.pack()

lv2 = Button(window, text='PLAY', command=lambda: lvStart(2, 'Pontos: 1', lv2, [40, 40], [240, 160]), font='Time 40 bold', bg=FOOD)
lv3 = Button(window, text='PLAY', command=lambda: lvStart(3, 'Pontos: 2', lv3, [200, 240], [400, 0]), font='Time 40 bold', bg=FOOD)
lv4 = Button(window, text='PLAY', command=lambda: lvStart(4, 'Pontos: 3', lv4, [0, 0], [400, 200]), font='Time 40 bold', bg=FOOD)
lv5 = Button(window, text='PLAY', command=lambda: lvStart(5, 'Pontos: 4', lv5, [240, 0], [240, 440]), font='Time 40 bold', bg=FOOD)

levels = {
    2: { 'button': lv2, 'walls': [(0, 80), (0, 40), (40, 0), (80, 40), (80, 80), (0, 0), (80, 0), (80, 120), (80, 160), (80, 200), (80, 280), (80, 320), (80, 360), (80, 400), (120, 480), (80, 480), (40, 480), (0, 480), (0, 440), (0, 400), (0, 360), (0, 320), (0, 240), (0, 200), (0, 160), (0, 120), (0, 280), (160, 480), (160, 440), (160, 360), (160, 400), (160, 320), (160, 280), (160, 240), (160, 200), (160, 120), (160, 160), (160, 80), (120, 0), (160, 0), (200, 0), (240, 0), (200, 80), (240, 80), (280, 0), (280, 80), (280, 120), (360, 0), (320, 0), (360, 40), (360, 80), (360, 120), (360, 160), (280, 160), (240, 240), (240, 280), (240, 320), (240, 360), (240, 400), (200, 480), (240, 480), (280, 480), (320, 480), (280, 240), (280, 200), (320, 240), (360, 240), (440, 200), (440, 240), (440, 120), (440, 160), (440, 80), (400, 0), (440, 0), (480, 0), (280, 400), (320, 400), (360, 480), (400, 480), (440, 480), (440, 440), (440, 360), (360, 360), (360, 400), (440, 400), (360, 320), (360, 280), (440, 320), (440, 280), (80, 240), (240, 200)] },
    3: { 'button': lv3, 'walls': [(0, 360), (0, 320), (0, 280), (360, 40), (440, 0), (440, 40), (440, 80), (440, 120), (400, 120), (360, 120), (320, 120), (320, 40), (280, 40), (240, 40), (200, 40), (160, 40), (120, 40), (80, 40), (40, 40), (0, 160), (0, 200), (0, 120), (0, 240), (280, 120), (240, 120), (160, 120), (200, 120), (120, 120), (80, 120), (0, 400), (40, 400), (80, 400), (120, 400), (160, 400), (200, 400), (240, 400), (280, 400), (320, 400), (360, 400), (400, 400), (400, 360), (400, 320), (400, 280), (400, 240), (400, 200), (80, 160), (80, 200), (80, 240), (80, 320), (80, 280), (120, 320), (160, 320), (200, 320), (240, 320), (280, 320), (320, 320), (320, 280), (320, 240), (320, 200), (280, 200), (400, 160), (240, 200), (160, 200), (200, 200), (160, 240), (400, 80)] },
    4: { 'button': lv4, 'walls': [(80, 0), (120, 40), (40, 80), (80, 120), (160, 80), (120, 160), (200, 120), (240, 160), (160, 200), (240, 200), (240, 240), (240, 280), (200, 320), (160, 240), (120, 280), (160, 360), (120, 400), (40, 360), (0, 400), (80, 480), (120, 480), (160, 480), (200, 480), (240, 480), (280, 480), (320, 320), (320, 440), (320, 480), (320, 360), (160, 400), (240, 400), (200, 400), (240, 360), (240, 320), (320, 280), (320, 240), (320, 160), (320, 200), (280, 80), (240, 40), (280, 40), (360, 40), (360, 80), (360, 120), (360, 160), (360, 200), (360, 240), (400, 240), (440, 80), (440, 40), (440, 120), (480, 40), (320, 40), (360, 360), (400, 320), (440, 400), (440, 440), (400, 440), (360, 440), (160, 320), (40, 240), (0, 200), (80, 160), (0, 160), (120, 0), (160, 0), (400, 0)] },
    5: { 'button': lv5, 'walls': [(200, 440), (160, 440), (120, 440), (80, 440), (40, 440), (0, 440), (0, 400), (280, 440), (320, 440), (360, 440), (400, 440), (440, 440), (480, 440), (480, 400), (480, 360), (0, 360), (0, 320), (0, 0), (40, 0), (80, 0), (120, 0), (160, 0), (200, 0), (280, 0), (320, 0), (360, 0), (400, 0), (480, 0), (440, 0), (480, 200), (480, 320), (480, 280), (480, 240), (480, 160), (480, 120), (480, 80), (480, 40), (0, 40), (0, 160), (0, 240), (0, 280), (0, 200), (0, 120), (0, 80), (280, 80), (160, 80), (240, 120), (120, 80), (200, 160), (120, 160), (160, 160), (80, 80), (40, 80), (80, 160), (40, 240), (120, 240), (160, 240), (200, 240), (240, 240), (280, 200), (320, 160), (360, 120), (360, 80), (440, 80), (440, 120), (440, 160), (400, 200), (400, 240), (440, 280), (320, 280), (320, 320), (280, 320), (280, 360), (360, 320), (240, 320), (200, 320), (160, 320), (200, 400), (200, 360), (120, 320), (80, 320), (120, 360), (160, 360), (400, 360), (360, 360), (240, 200), (400, 80)]}
}


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
window.bind('<K>',
            lambda event: game_over(lv2, '2'))
window.bind('<M>',
            lambda event: game_over(lv3, '3'))
window.bind('<P>',
            lambda event: game_over(lv4, '4'))
window.bind('<H>',
            lambda event: game_over(lv5, '5'))

snake = [0,0]
walls = [(80, 0), (120, 0), (160, 0), (200, 0), (240, 0), (280, 0), (320, 0), (360, 0), (400, 0), (440, 0), (480, 0), (0, 80), (120, 80), (160, 80), (200, 80), (240, 80), (280, 80), (320, 80), (360, 80), (360, 120), (360, 160), (480, 80), (440, 80), (440, 120), (440, 160), (480, 160), (480, 200), (480, 240), (480, 280), (320, 160), (280, 160), (280, 120), (200, 120), (200, 160), (160, 160), (120, 160), (320, 240), (280, 240), (360, 240), (40, 80), (40, 120), (40, 160), (40, 200), (40, 240), (40, 280), (120, 280), (80, 280), (120, 240), (200, 240), (200, 280), (200, 320), (160, 360), (40, 360), (40, 400), (480, 40), (80, 400), (120, 400), (160, 400), (200, 400), (240, 320), (280, 320), (320, 400), (320, 320), (360, 320), (480, 320), (480, 360), (480, 400), (480, 440), (480, 480), (360, 480), (400, 440), (80, 480), (120, 480), (160, 480), (40, 480), (200, 480), (400, 360), (400, 320), (440, 400), (240, 400), (240, 360), (360, 440), (320, 440)]

food = [400, 400]




window.mainloop()