import pygame

# Always do this to initialize pygame
pygame.init()

# This is where you set your window that you will be seeing things happen in
win = pygame.display.set_mode((500, 500))

# This is where you name your display in pygame
pygame.display.set_caption("Learning pygame")

# These are the variables of your character
x = 50
y = 5
width = 40
height = 60
vel = 5

# This is where we make our jump
isJump = False
jumpCount = 10

# This is our loop for the game
run = True
while run:
    pygame.time.delay(100)

    # This is where the game checks any events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # This tells the game to recognize a key being pressed and what to do with is
    keys = pygame.key.get_pressed()

    # This is where you give the key commands. the "and" statement is where we stop our object from going off screen
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    # In this "and" statement we need to use the screen width minus the width of the character or this will let us go past the screen and the size of the character.
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel

    # This is how we make it so once in the air other movement wont happen
    if not (isJump):

        # The y statements are similar to the x but now we are using the height of the character.
        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel

        # This is where we give our jump a key binding and its properties
        if keys[pygame.K_SPACE]:
            isJump = True
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

    # This has  us fill the background so we don't keep duplicating our character
    win.fill((0, 0, 0))

    # This is where it creates or "draws" your object
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    # This tells pygame to put the thing in the display
    pygame.display.update()
pygame.quit()
