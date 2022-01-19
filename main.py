import pygame as pg
import sys

pg.init()
screen = pg.display.set_mode((480, 354))
pg.display.set_caption("Piškvorky")

class TICTACTOE():
    def __init__(self):
        self.x = pg.image.load("Veci/x.jpg").convert_alpha()
        self.x_r = self.x.get_rect()

        self.table = pg.image.load("Veci/table.jpg").convert_alpha()
        self.table_r = self.table.get_rect(topleft=(0,0))
        self.running = True


        self.clock = pg.time.Clock()
    def main(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            if self.running == True:
                screen.fill("black")
                screen.blit(self.table, self.table_r)



            pg.display.update()
            self.clock.tick(60)

x=TICTACTOE()
x.main()
