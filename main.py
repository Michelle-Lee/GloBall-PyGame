import pygame
from Player import Player

background = pygame.image.load('pics/background.png')

WIN_HEIGHT = background.get_height()
WIN_WIDTH = background.get_height() + 30
BG_WIDTH = background.get_width()

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("First Game")


def redrawGameWindow():
    WIN.blit(background, (player.bgX, 0))    # win.blit will fill window with loaded image
    player.draw(WIN)
    pygame.display.update()


player = Player(20, WIN_HEIGHT - (144 + 50), 50, 50)
# player.displayCharacter(WIN)
# pygame.display.update()

clock = pygame.time.Clock()
run = True
while run:

    clock.tick(24)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.x > player.vel:
        player.moveLeft(WIN_WIDTH)

    elif keys[pygame.K_RIGHT] and player.x < WIN_WIDTH - player.width - player.vel:
        player.moveRight(WIN_WIDTH, BG_WIDTH)

    else:
        player.isWalk = False
        player.walkCount = 0


    
    if not(player.isJump):
        if keys[pygame.K_SPACE]:
            player.isJump = True
            player.isWalk = False
    else: 
        player.jump()

    redrawGameWindow()


pygame.quit()