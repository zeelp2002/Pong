import pygame
import random
import time

class snake():
    def __init__(self, display, gridsize, x = 200, y = 200):
        self.display = display
        self.gridsize = gridsize
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0
        self.snakelist = []
        self.start = (x,y)
        self.snakelist.append(self.start)
        self.snakelength = 3
        
    def turnleft(self):
        if self.x_change < 0:
            return
        self.x_change -= self.gridsize
        self.y_change = 0
    def turnright(self):
        if self.x_change > 0:
            return
        self.x_change += self.gridsize
        self.y_change = 0
    def turnup(self):
        if self.y_change <0:
            return
        self.x_change = 0
        self.y_change -= self.gridsize
        
    def turndown(self):
        if self.y_change > 0:
            return
        self.x_change = 0
        self.y_change += self.gridsize
    
    def addsegment(self):
        self.snakelength += 1
        
    def move(self):
        self.x += self.x_change
        self.y += self.y_change
        self.snakehead = (self.x, self.y)
        if self.snakelength > 3:
            if self.snakehead in self.snakelist:
                return False
        self.snakelist.append(self.snakehead)
        if len(self.snakelist) > self.snakelength:
            del self.snakelist[0]
