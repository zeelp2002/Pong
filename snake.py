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

class apple():
    #return a (x,y)
    def __init__(self, screenwidth, screenheight, gridsize):
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.gridsize = gridsize
        self.x = round(random.randrange(0, self.screenwidth - self.gridsize)/self.gridsize)*self.gridsize
        self.y = round(random.randrange(0, self.screenheight - self.gridsize)/self.gridsize)*self.gridsize
    
    def newloc(self, snake):
        badspawn = True
        while badspawn == True:
            self.x = round(random.randrange(0, self.screenwidth - self.gridsize)/self.gridsize)*self.gridsize
            self.y = round(random.randrange(0, self.screenheight - self.gridsize)/self.gridsize)*self.gridsize
            badspawn = False
            for position in snake.snakelist:
                if position[0] == self.x and position[1] == self.y:
                    badspawn = True
                    break
                else:
                    badspawn = False

class game():
    black = (0,0,0)
    red = (200, 0, 0)
    green = (0, 200, 0)
    blue = (0, 0, 200)
    white = (240, 240, 240)
    #
    def __init__(self, screenwidth, screenheight, gridsize):
        pygame.init()
        self.running = True
        self.endgame = False
        self.pregame = True
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.gridsize = gridsize
        self.display = pygame.display.set_mode((self.screenwidth, self.screenheight))
        pygame.display.set_caption('Snake')
        
        self.clock = pygame.time.Clock()
        self.snakespeed = 15
        
        self.snake = snake(self.display, self.gridsize)
        self.apple = apple(self.screenwidth, self.screenheight, self.gridsize)
        
    def game_loop(self):
        while self.running == True:

            if self.pregame == True:
                while self.pregame == True:
                    self.display.fill(self.black)
                    self.message('Welcome to Snake! Press P to Play!', self.screenwidth/2, self.screenheight/2)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p:
                                self.pregame = False 
                            if event.key == pygame.K_ESCAPE:
                                pygame.quit()
                                self.running = False
                                
            if self.endgame == True:
                while self.endgame == True:
                    self.display.fill(self.black)
                    self.message('You lost! Press P to play again or Q to quit.', self.screenwidth/2, self.screenheight/2)
                    self.scoremessage = ('Your final score was: ') + self.printscore
                    self.message(self.scoremessage, self.screenwidth/2, (self.screenheight/2 + 64))       
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p:
                                main()
                            if event.key == pygame.K_q:
                                self.running = False
                                pygame.quit()
                            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                   
                    if event.key == pygame.K_RIGHT:
                        self.snake.turnright()
                    if event.key == pygame.K_LEFT:
                        self.snake.turnleft()
                    if event.key == pygame.K_UP:
                        self.snake.turnup()
                    if event.key == pygame.K_DOWN:
                        self.snake.turndown()
                    
            if self.snake.move() == False:
                self.endgame = True
            
            if self.boundarycollision() == True:
                self.endgame = True
            
            if self.applecollision() == True:
                self.snake.addsegment()
                self.apple.newloc(self.snake)
                
            self.display.fill(self.black)
            
            self.printscore = str(self.score())
            self.message(self.printscore, 32, 32)
            
            self.drawapple(self.apple)
            self.drawsnake(self.snake)
            
            pygame.display.flip()
            self.clock.tick(self.snakespeed)
            
            
    def drawsnake(self, snake):
        for segment in self.snake.snakelist:
            pygame.draw.rect(self.display, self.white, (segment[0], segment[1], snake.gridsize, snake.gridsize))
    
    def drawapple(self, apple):
        pygame.draw.rect(self.display, self.green, (self.apple.x, self.apple.y, apple.gridsize, apple.gridsize))
    def boundarycollision(self):
       if self.snake.x < 0 or self.snake.y < 0 or self.snake.x > self.screenwidth - self.gridsize or self.snake.y > self.screenheight - self.gridsize:
            return True
       else:
            return False
    
    def applecollision(self):
        if self.snake.x == self.apple.x and self.snake.y == self.apple.y:
            return True
        else:
            return False
     
    def message(self, message, x, y):
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.text = self.font.render(message, True, self.white)
        self.textRect = self.text.get_rect()
        self.textRect.center = (x,y)
        self.display.blit(self.text, self.textRect)

    def score(self):
        counter = -3
        for i in range(self.snake.snakelength):
            counter += 1
        return counter


def main():
    playgame = game(1500, 700, 50)
    playgame.game_loop()
    
if __name__ == '__main__':
    main()