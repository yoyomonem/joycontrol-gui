import pygame

"""
to change a button's key set the value to pygame.K_(your key) example:
yKey = pygame.K_e
if you want to disable a button set the value to None, example:
rstickKeyClick = None
"""

switchMac = "DC:68:EB:71:CF:F1" # your mac address here 
lstickKeyUp = pygame.K_w
lstickKeyDown = pygame.K_s
lstickKeyLeft = pygame.K_a
lstickKeyRight = pygame.K_d
lstickKeyClick = pygame.K_f
aKey = pygame.K_SPACE
bKey = pygame.K_BACKSPACE
xKey = pygame.K_q
yKey = pygame.K_e
lKey = pygame.K_t
rKey = pygame.K_y
zlKey = pygame.K_c
zrKey = pygame.K_b
minusKey = pygame.K_ESCAPE
dpadUp = pygame.K_UP
dpadDown = pygame.K_DOWN
dpadLeft = pygame.K_LEFT
dpadRight = pygame.K_RIGHT
rstickKeyClick = pygame.K_l
plusKey = pygame.K_BACKSLASH
nfcKey = pygame.K_h
catchMouse = False # makes sure mouse stays in the middle of the window use alt+e to toggle
mouseAsRstick = False # experimental, also turn on catch mouse 
rstickSenstivity = 14