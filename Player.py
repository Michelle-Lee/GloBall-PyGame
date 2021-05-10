import pygame
class Player(object):
    walkRight = [pygame.image.load('pics/chibi-ball-roll1.png'), pygame.image.load('pics/chibi-ball-roll2.png'), pygame.image.load('pics/chibi-ball-roll3.png') , pygame.image.load('pics/chibi-ball-roll4.png'), pygame.image.load('pics/chibi-ball-roll5.png'), pygame.image.load('pics/chibi-ball-roll6.png'), pygame.image.load('pics/chibi-ball-roll7.png'), pygame.image.load('pics/chibi-ball-roll8.png')]
    walkLeft = [pygame.image.load('pics/chibi-ball-roll8.png'), pygame.image.load('pics/chibi-ball-roll7.png'), pygame.image.load('pics/chibi-ball-roll6.png'), pygame.image.load('pics/chibi-ball-roll5.png'), pygame.image.load('pics/chibi-ball-roll4.png'), pygame.image.load('pics/chibi-ball-roll3.png'), pygame.image.load('pics/chibi-ball-roll2.png'), pygame.image.load('pics/chibi-ball-roll1.png')]
    idleLeft = pygame.image.load('pics/chibi-ball.png')
    idleRight = pygame.image.load('pics/chibi-ball.png')
    # jumpLeft = pygame.image.load('')
    # jumpRight = pygame.image.load('')
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 30
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = True
        self.isWalk = False
        self.walkCount = 0
        self.bgX = 0

    def displayCharacter(self, win):
        win.blit(self.idleLeft, (self.x, self.y))

    def draw(self, win):
        if self.walkCount + 1 >= 24:
            self.walkCount = 0

        if self.isWalk or self.isJump:
            if self.left:
                win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1

        # elif isJump:
        #     if left:
        #         WIN.blit(jumpLeft, (x, y))
        #     elif right:
        #         WIN.blit(jumpRight, (x, y))

        else:
            if self.left:
                win.blit(self.idleLeft, (self.x, self.y))
            elif self. right:
                win.blit(self.idleRight, (self.x, self.y))

    def moveLeft(self, win_width):
        if ((self.bgX == 0 and self.x > self.vel) or self.x > win_width * (1/3) + self.vel):
            self.x -= self.vel
        elif (self.x <= win_width * (1/3) + self.vel):
            self.bgX += self.vel
        self.isWalk = True
        self.left = True
        self.right = False

    def moveRight(self, win_width, bg_width):
        # if (self.bgX >= bg_width - win_width):
        #     self.bgX = bg_width - win_width
        if ((self.bgX == bg_width - win_width and self.x < win_width - self.width - self.vel) or self.x <= win_width * (2/3) - self.vel):
            self.x += self.vel
            print("testing")
        elif (self.bgX > -(bg_width - win_width) and self.x >= win_width * (2/3) - self.vel and self.x < win_width - self.width - self.vel):
            self.bgX -= self.vel
            print("more testing")
        

        self.isWalk = True
        self.left = False
        self.right = True

    def jump(self):
        if self.jumpCount >= -10:
            neg = 1
            if self.jumpCount < 0:
                neg = -1
            self.y -= (self.jumpCount ** 2) * 0.5 * neg
            self.jumpCount -= 1
        else:
            self.isJump = False
            self.jumpCount = 10
