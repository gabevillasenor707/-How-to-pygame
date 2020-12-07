import pygame

# Always do this to initialize pygame
pygame.init()

# This is where you set your window that you will be seeing things happen in
win = pygame.display.set_mode((500, 480))

# This is where you name your display in pygame
pygame.display.set_caption("Learning pygame")

# This is where we are loading all our images and this will be specific to your directories
walkRight = [pygame.image.load('/Users/gabe/Desktop/Game/R1.png'), pygame.image.load('/Users/gabe/Desktop/Game/R2.png'), pygame.image.load('/Users/gabe/Desktop/Game/R3.png'), pygame.image.load('/Users/gabe/Desktop/Game/R4.png'), pygame.image.load('/Users/gabe/Desktop/Game/R5.png'), pygame.image.load('/Users/gabe/Desktop/Game/R6.png'), pygame.image.load('/Users/gabe/Desktop/Game/R7.png'), pygame.image.load('/Users/gabe/Desktop/Game/R8.png'), pygame.image.load('/Users/gabe/Desktop/Game/R9.png')]
walkLeft = [pygame.image.load('/Users/gabe/Desktop/Game/L1.png'), pygame.image.load('/Users/gabe/Desktop/Game/L2.png'), pygame.image.load('/Users/gabe/Desktop/Game/L3.png'), pygame.image.load('/Users/gabe/Desktop/Game/L4.png'), pygame.image.load('/Users/gabe/Desktop/Game/L5.png'), pygame.image.load('/Users/gabe/Desktop/Game/L6.png'), pygame.image.load('/Users/gabe/Desktop/Game/L7.png'), pygame.image.load('/Users/gabe/Desktop/Game/L8.png'), pygame.image.load('/Users/gabe/Desktop/Game/L9.png')]
bg = pygame.image.load('/Users/gabe/Desktop/Game/bg.jpg')
char = pygame.image.load('/Users/gabe/Desktop/Game/standing.png')

# This is the clock command
clock = pygame.time.Clock()

# These are the variables of your character
x = 50
y = 400
width = 64
height = 64
vel = 5

# This is where we make our jump
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0

def  redrawGameWindow():
    global walkCount

    # This has us put our image as a background
    win.blit(bg, (0,0))

    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
    # This tells pygame to put the thing in the display
    pygame.display.update()

# This is our Mainloop for the game
run = True
while run:
    # Clock sets our fps for the game we are using 27 because the amount of images we have
    clock.tick(27)

    # This is where the game checks any events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # This tells the game to recognize a key being pressed and what to do with is
    keys = pygame.key.get_pressed()

    # This is where you give the key commands. the "and" statement is where we stop our object from going off screen
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False

    # In this "and" statement we need to use the screen width minus the width of the character or this will let us go past the screen and the size of the character.
    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
        right = True
        left = False
    # This is so when not doing anything we don't have a change in our sprite
    else:
        right = False
        left = False
        walkCount = 0

    # This is how we make it so once in the air other movement wont happen
    if not (isJump):

        # This is where we give our jump a key binding and its properties
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    # Here is where we make the jump happen but also bring our character down so they dont just go up in the air or float
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()


pygame.quit()
