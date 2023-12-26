import random
import tkinter
import pygame
pygame.init()
pygame.display.set_mode((600,400))

def move_player(event):
    if event.keysym == 'w':
        canvas.move(player, 0, -20)
    if event.keysym == 'a':
        canvas.move(player, -20, 0)
    if event.keysym == 's':
        canvas.move(player, 0, 20)
    if event.keysym == 'd':
        canvas.move(player, 20, 0)



def create_point():
    global point
    point_pos = (random.randint(a=1, b=400), random.randint(1, 400))
    point = canvas.create_oval(point_pos[0], point_pos[1], point_pos[0] + 50, point_pos[1] + 50, fill='#191970')


def restart_game():
    global canvas, player
    start_pos = (random.randint(a=1, b=400), random.randint(1, 400))
    player = canvas.create_rectangle(start_pos[0], start_pos[1], start_pos[0] + 50, start_pos[1] + 50, fill='#FF0000')
    create_point()
    restart_bt.config(state='disabled')


root = tkinter.Tk()
root.title("mg")
root.geometry("200x200")

label_score = tkinter.Label(root, text="я котик")
restart_bt = tkinter.Button(root, text="старт", command=restart_game)
canvas = tkinter.Canvas(root, width=400, height=400, bg="#98FB98")

player = ''
point = ''
label_score.pack()
restart_bt.pack()
canvas.pack()
root.bind('<KeyPress>',move_player)
root.mainloop()