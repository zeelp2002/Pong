"""
* Author: Zeel P
* Date: July 15, 2020 
 * Project: 2 Player Pong Game
 * Decription: A game where the objective to not let the ball leave the sides of the screen
"""

    #CONTROL
# Player 1: USE ARROW KEYS
#   Up key allows paddle to move up
#   Down key allows paddle to move down

# Player 2: USE ARROW KEYS
#   'A' key allows paddle to move up
#   'Z' key allows paddle to move down


import pygame
import random
import math

 
#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Sets the screen 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
BALL_SIZE = 15

# Set the height and width of the screen
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

class Ball: 
    # Class to keep track of the ball's location and vector.
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0

class Paddle:
    # Class to keep track of the paddles location and vector
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
 
def make_ball():
    # Function to make a new, random ball.
    ball = Ball()
    # Starting position of the ball.
    ball.x = 400
    ball.y = 200
 
    # Speed and direction of rectangle  
    ball.change_x = 2
    ball.change_y = 3

    return ball
 
def makeRightPaddle():
    rightPaddle = Paddle()
    rightPaddle.x = SCREEN_WIDTH - 50
    rightPaddle.y = SCREEN_HEIGHT/2
    rightPaddle.width = 10
    rightPaddle.height = 100
    
    return rightPaddle

def makeLeftPaddle():
    leftPaddle = Paddle()
    leftPaddle.x = 40
    leftPaddle.y = SCREEN_HEIGHT/2
    leftPaddle.width = 10
    leftPaddle.height = 100

    return leftPaddle

def title(x, y):
    font = pygame.font.Font('freesansbold.ttf', 64)
    text = font.render('Pong', True, WHITE)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)

def leftScore(x, y, score):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(score), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)

def rightScore(x, y, score):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(score), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)

def gameOver(x, y, winner):
    font = pygame.font.Font('freesansbold.ttf', 40)
    text = font.render(str(winner) + ' has won the game', True, WHITE)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)


def main():
    pygame.init()

    #Score
    rScore = 0
    lScore = 0
 
    #Sets the title to Pong
    pygame.display.set_caption("Pong")
 
    # Loop until the user clicks the close button.
    running = True
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    #calls make functions 
    ball = make_ball()
    rightPaddle = makeRightPaddle()
    leftPaddle = makeLeftPaddle()

    #sets the move functions
    rightMoveUp = False
    rightMoveDown = False
    leftMoveUp = False
    leftMoveDown = False


                            #Main Program Loop
    while running:
                #Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                 #Escape quits the game
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit

                        #Right Paddle
                    #Up key moves paddle up
                elif event.key == pygame.K_UP:
                    rightMoveUp = True
                    #Down key moves paddle down
                elif event.key == pygame.K_DOWN:
                    rightMoveDown = True

                    #Left Paddle
                # A key moves the paddle up
                elif event.key == pygame.K_a:
                    leftMoveUp = True
                # Z key moved the paddle down
                elif event.key == pygame.K_z:
                    leftMoveDown = True

            elif event.type == pygame.KEYUP:
                rightMoveUp = False
                rightMoveDown = False
                leftMoveUp = False
                leftMoveDown = False

            #Allows user to hold down buttons 
        if rightMoveUp == True:
            rightPaddle.y -= 3
        if rightMoveDown == True:
            rightPaddle.y += 3
        if leftMoveUp == True:
            leftPaddle.y -= 3
        if leftMoveDown == True:
            leftPaddle.y += 3

                # Logic
            # Move the ball's center
        ball.x += ball.change_x
        ball.y += ball.change_y
 
            # Bounce the ball if needed
            # Count score
        if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
            ball.change_y *= -1
        elif ball.x > SCREEN_WIDTH - BALL_SIZE :
            ball.x = 400
            ball.y = 200
            ball.change_x = 3
            ball.change_y = 2
            rScore += 1     
        elif ball.x < BALL_SIZE:
            ball.x = 400
            ball.y = 200
            ball.change_x = 3
            ball.change_y = 2
            lScore += 1
              
            # Bounce ball off Paddles
        if (ball.x + BALL_SIZE <= rightPaddle.x + rightPaddle.width and ball.x + BALL_SIZE >= rightPaddle.x) and (ball.y <= rightPaddle.y + rightPaddle.height and ball.y > rightPaddle.y):
            ball.change_x *= -1
        if (ball.x - BALL_SIZE<= leftPaddle.x + leftPaddle.width and ball.x - BALL_SIZE>= leftPaddle.x) and (ball.y <= leftPaddle.y + leftPaddle.height and ball.y >= leftPaddle.y):
            ball.change_x *= -1
        
            # Paddles contrained to screen
        if rightPaddle.y < 0 :
            rightPaddle.y = 0
        elif rightPaddle.y > SCREEN_HEIGHT - 100:
            rightPaddle.y = SCREEN_HEIGHT - 100
        elif leftPaddle.y < 0:
            leftPaddle.y = 0
        elif leftPaddle.y > SCREEN_HEIGHT - 100:
            leftPaddle.y = SCREEN_HEIGHT - 100


            #Drawing
        # Set the screen background
        screen.fill(BLACK)
 
        # Draw the ball and paddles
        pygame.draw.circle(screen, WHITE, [ball.x, ball.y], BALL_SIZE)
        pygame.draw.rect(screen, WHITE, (rightPaddle.x, rightPaddle.y, rightPaddle.width, rightPaddle.height))
        pygame.draw.rect(screen, WHITE, (leftPaddle.x, leftPaddle.y, leftPaddle.width, leftPaddle.height))

        #Set the frame rate
        clock.tick(60)


        #Display all text on screen
        title(400, 50)
        leftScore(30, 30, lScore)
        rightScore(SCREEN_WIDTH - 30, 30, rScore)
        
        #Game Over Screen
        if(rScore == 7):
            winner = 'Right Player'
            gameOver(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50, winner)
            ball.change_x = 0
            ball.change_y = 0
        elif(lScore == 7):
            winner = 'Left Player'
            gameOver(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50, winner)
            ball.change_x = 0
            ball.change_y = 0
 
        #Update Screen
        pygame.display.flip()
        pygame.display.update()

 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()