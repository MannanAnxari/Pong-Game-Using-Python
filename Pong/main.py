# import sys
# import pygame
# from pygame.locals import *
# import random

# black = (0, 0, 0)
# FPS = 32
# SCREENWIDTH = 858
# SCREENHEIGHT = 525
# SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
# PLAYER0 = pygame.image.load('gallery/sprites/side0.png').convert_alpha()
# PLAYER1 = pygame.image.load('gallery/sprites/side1.png').convert_alpha()
# BALL = pygame.image.load('gallery/sprites/ball.png').convert_alpha()
# BG = pygame.image.load('gallery/sprites/bg.png').convert_alpha()
# CL = pygame.image.load('gallery/sprites/centerLine.png').convert_alpha()


# def main_Game():
#     ballx = int((SCREENHEIGHT - BALL.get_width()) / 2)
#     bally = int((SCREENWIDTH - BALL.get_width()) / 2)
#     linx = int(SCREENWIDTH / 2)
#     playerx0 = 10
#     playery0 = int((SCREENHEIGHT - PLAYER1.get_height()) / 2)
#     playerx1 = int((SCREENWIDTH - PLAYER1.get_width()) - 10)
#     playery1 = int((SCREENHEIGHT - PLAYER1.get_height()) / 2)

#     FPSCLOCK = pygame.time.Clock()

#     player1AccV = -9
#     players = False
#     player0_Up = False
#     player0_Down = False
#     player1_Up = False
#     player1_Down = False
#     ball_Move = False
#     dX = 0

#     while True:
#         # SCREEN.fill(black)
#         SCREEN.blit(BG, (0, 0))
#         SCREEN.blit(CL, (linx, 0))
#         for event in pygame.event.get():
#             if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
#                 pygame.quit()
#                 sys.exit()

#             if event.type == KEYDOWN:
#                 if event.key == K_UP:
#                     player1_Up = True
#                 if event.key == K_DOWN:
#                     player1_Down = True
#                 if event.key == K_a:
#                     player0_Up = True
#                 if event.key == K_z:
#                     player0_Down = True
#             if event.type == KEYUP:
#                 if event.key == K_UP:
#                     player1_Up = False
#                 if event.key == K_DOWN:
#                     player1_Down = False
#                 if event.key == K_a:
#                     player0_Up = False
#                 if event.key == K_z:
#                     player0_Down = False
#             # if event.type == KEYUP:
#             #     if event.key == K_UP:
#             #         move_Left = False
#             #     if event.key == K_RIGHT:
#             #         move_Right = False
#             # if event.type == KEYDOWN:
#             #     if event.key == K_SPACE:
#             #         # ball_Move = True
#             #         if ball_Move == True:
#             #             ballx += 10
#             #             bally += 10
#             #         elif ballx > 400:
#             #             bally -= 10
#             #             ballx -= 10
#             #             print('\nball y', bally)
#             #             print('ball x', ballx)
#                 # else:
#                 #     return
# # yayayya
#         if player0_Up:
#             playery0 -= 10

#         if player0_Down:
#             playery0 += 10

#         if player1_Up:
#             playery1 -= 10

#         if player1_Down:
#             playery1 += 10

#         # if playerx < 0:
#         #     playerx = 858
#         # elif playerx > 858:
#         #     playerx = 0
# # asdhilausdh
#         # if ball_Move:
#         #     ballx += 5
#         #     bally += 5
#         #     if ballx > 400:
#         #         ballx -= 5
#         #         bally -= 5

#         SCREEN.blit(BALL,  (bally, ballx))
#         SCREEN.blit(PLAYER0, (playerx0, playery0))
#         SCREEN.blit(PLAYER1, (playerx1, playery1))
#         pygame.display.update()
#         FPSCLOCK.tick(FPS)


# if __name__ == '__main__':
#     main_Game()


from tkinter import *
import random
import time


class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 2
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos):
            self.y = -2
        if pos[0] <= 0:
            self.x = 2
        if pos[2] >= self.canvas_width:
            self.x = -2


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -3

    def turn_right(self, evt):
        self.x = 3


tk = Tk()
tk.title("Bouncing Ball Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'gray')

while 1:
    if not ball.hit_bottom:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
