import pygame

# Always do this to initialize pygame
pygame.init()

# This is where you set your window that you will be seeing things happen in
win = pygame.display.set_mode((600, 800))

# This is where you name your display in pygame
pygame.display.set_caption("Learning pygame")

# These are the variables of your character
x = 50
y = 5
width = 40
height = 60
vel = 5

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

    # This is where you give the key commands
    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel

    # This has  us fill the background so we don't keep duplicating our character    
    win.fill((0, 0, 0))

    # This is where it creates or "draws" your object
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    # This tells pygame to put the thing in the display
    pygame.display.update()
pygame.quit()
