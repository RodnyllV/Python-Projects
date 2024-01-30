from unittest import case
import pygame
import math

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()
deltaTime = 0
running = True

# Dynamic variables
velocity = pygame.Vector2(0, 0)
mouseSpeed = pygame.Vector2(0, 0)
lastMousePosition = pygame.mouse.get_pos()
fling = False
currentPosition = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Static variables
gravity = 9.8
ballWidth = 35

while running:
    for event in pygame.event.get(): # Exits the window once the "X" button is clicked
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("black") # Sets the background as black

    ball = pygame.draw.circle(screen, "white", currentPosition, ballWidth, 0) # Creates a new ball every frame from the previous position
    
    if pygame.mouse.get_pressed()[0] and ball.collidepoint(pygame.mouse.get_pos()): # Change the balls position when it gets clicked to follow the mouse
        currentPosition = pygame.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        ball.move(currentPosition.x, currentPosition.y)

        fling = True
    else: # Once the mouse button click is released, fling the ball at approx the same speed as the mouse
        if fling == True:
            fling = False
            velocity = mouseVelocity * 2.5
    
    pygame.display.flip()
    
    mouseVelocity = pygame.Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]) - lastMousePosition # Gets mouse velocity
    
    deltaTime = clock.tick(60) / 1000 # Get the time intervals in 60 fps
    
    lastMousePosition = pygame.mouse.get_pos()

    ball.move_ip(velocity.x,  velocity.y) # Change the ball position from the current one by the given increments
    currentPosition += velocity
    velocity -= pygame.Vector2(0, -9.8 * deltaTime)
    
    rightBound = pygame.display.get_window_size()[0] - (ballWidth / 2) # Right bound of the screen
    bottomBound = pygame.display.get_window_size()[1] - (ballWidth / 2) # Bottom bound of the screen

    bounceNormal = pygame.Vector2()

    match [ball.left < 0, ball.right > rightBound]: # Get the 2D normals of the window (top and bottom)
        case [True, False]:
            bounceNormal = pygame.Vector2(1, 0)
            ball.move_ip(-abs(ball.left), 0)
        case [False, True]:
            bounceNormal = pygame.Vector2(-1, 0)
            ball.move_ip(ball.right - rightBound, 0)
    
    match [ball.top < 0, ball.bottom > bottomBound]: # Get the 2D normals of the window (left and right)
        case [True, False]:
            bounceNormal = pygame.Vector2(0, -1)
            ball.move_ip(abs(ball.top), 0)
        case [False, True]:
            bounceNormal = pygame.Vector2(0, 1)
            ball.move_ip(ball.bottom - bottomBound, 0)

    if (ball.left < 0 or ball.right > rightBound) or (ball.top < 0 or ball.bottom > bottomBound): # Calculate how the vector should be reflected once hitting a surface
        velocity = (velocity - (2 * (velocity.dot(bounceNormal))) * bounceNormal) * .67

pygame.quit()
