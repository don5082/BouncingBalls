import sys

import numpy as np
import pygame
import Simulator

GRAVITY = 9.81
# GRAVITY = 0
class Ball:
    x = 0.0
    y = 0.0
    x_velo = 0.0
    y_velo = 0.0
    radius = 1

    def __init__(self, x_pos, y_pos, radius, x_velo=0, y_velo=0):
        self.x = x_pos
        self.y = y_pos
        self.radius = radius
        self.x_velo = x_velo
        self.y_velo = y_velo

    def simulate(self, dt, x_acc=0, y_acc=GRAVITY):
        self.x += self.x_velo * dt
        self.y -= self.y_velo * dt

        self.x_velo += x_acc * dt
        self.y_velo -= y_acc * dt

        is_approaching_right = self.x_velo > 0
        is_approaching_left = self.x_velo < 0
        is_approaching_top = self.y_velo > 0
        is_approaching_bottom = self.y_velo < 0

        if ((self.x + self.radius) >= Simulator.W) and is_approaching_right :
            # print("hit right wall")
            if self.x_velo > Simulator.COLLISION_ENERGY_LOSS:
                self.x_velo = -(self.x_velo - Simulator.COLLISION_ENERGY_LOSS)
            else:
                self.x_velo = 0

        if (self.x - self.radius) <= 0 and is_approaching_left :
            # print("hit left wall")
            if -self.x_velo > Simulator.COLLISION_ENERGY_LOSS:
                self.x_velo = -(self.x_velo + Simulator.COLLISION_ENERGY_LOSS)
            else:
                self.x_velo = 0

        if (self.y + self.radius) >= Simulator.H and is_approaching_bottom:
            # print("hit bottom wall")
            if -self.y_velo > Simulator.COLLISION_ENERGY_LOSS:
                self.y_velo = -(self.y_velo + Simulator.COLLISION_ENERGY_LOSS)
            else:
                self.y_velo = 0

        if (self.y - self.radius) <= 0 and is_approaching_top:
            print("hit top wall")
            if self.y_velo > Simulator.COLLISION_ENERGY_LOSS:
                self.y_velo = -(self.y_velo - Simulator.COLLISION_ENERGY_LOSS)
            else:
                self.y_velo = 0


        if (self.x_velo == 0.0) and (self.y_velo == 0.0):
            print("ball is motionless")
            # pygame.display.quit()
            sys.exit()





    def draw(self, screen):
        pygame.draw.circle(screen, Simulator.WHITE, (self.x, self.y), self.radius)


    def set_x_velo(self, x_velo_new):
        self.x_velo = x_velo_new

    def set_y_velo(self, y_velo_new):
        self.y_velo = y_velo_new

    def set_velo(self, x_velo_new, y_velo_new):
        self.x_velo = x_velo_new
        self.y_velo = y_velo_new

    def print_ball(self, cur_time):
        print(f"time: {cur_time}")
        print(f"ball ID: {id(self)}, x_location: {self.x}, y_location: {self.y}")