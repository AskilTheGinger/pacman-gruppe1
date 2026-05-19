import pygame as pg
from constants import *
from board import Board
from pacman import PacMan

pg.init()
board = Board()
vindu = pg.display.set_mode(board.window_size())
clock = pg.time.Clock()


pacman = PacMan(3, 4)
tid=0
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        elif event.type ==pg.KEYDOWN and event.key==pg.K_UP:
            pacman.direction=[0,-1]
        elif event.type ==pg.KEYDOWN and event.key==pg.K_DOWN:
            pacman.direction=[0,1]
        elif event.type ==pg.KEYDOWN and event.key==pg.K_LEFT:
            pacman.direction=[-1,0]
        elif event.type ==pg.KEYDOWN and event.key==pg.K_RIGHT:
            pacman.direction=[1,0]

    # Tegn bakgrunn: (En slags "reset" av hele vinduet vårt)
    vindu.fill(BLACK)

    # Tegn brettet først, og pacman og andre ting "oppå":
    board.draw(vindu)

    # TODO: Oppdater objektene våre:


    # Tegn objektene våre:
    if tid%20==0:
        pacman.oppdater(board)
    pacman.draw(vindu)


    # Har alltid disse med til slutt:
    pg.display.flip()
    tid=tid+1
    clock.tick(FPS)


# While running er slutt: Avslutt pygame på en "ryddig måte":
pg.quit()
