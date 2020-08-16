import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # you saw nothing
from joycontrol_wrapper import joycontrolWrapper
import asyncio
import pygame
import config
from tkinter.filedialog import askopenfilename # using tkinter for file chooser 
from tkinter import Tk
pygame.init()
window_wdith = 200
window_height = 200
gameDisp = pygame.display.set_mode((window_wdith,window_height))
pygame.display.set_caption("joycontrol gui")
def maxMinCap(value,max,min):
    if value < min:
        return min
    elif value > max:
        return max
    else:
        return value
def text_object(text, font):
	textSurface = font.render(text, True , (0,0,0))
	return textSurface,textSurface.get_rect()
def statusText(content):
	txtSize = pygame.font.SysFont('arial',22)
	textSurf,textRect = text_object((content),txtSize)
	textRect = (10,0)
	gameDisp.blit(textSurf,textRect)
def nfcText(content):
	txtSize = pygame.font.SysFont('arial',22)
	textSurf,textRect = text_object((content),txtSize)
	textRect = (10,22)
	gameDisp.blit(textSurf,textRect)
async def main():
    filepath = ''
    nfcKeyOnce = False
    clock = pygame.time.Clock()
    xMoveCheck = False
    yMoveCheck = False
    cmToggled = False
    alt = False
    eToggle = False
    catchMouse = config.catchMouse
    gameDisp.fill((255,255,255))
    statusText("connecting...")
    pygame.display.update()
    wrapper = joycontrolWrapper()
    await wrapper.init(config.switchMac)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == config.lstickKeyUp:
                    await wrapper.moveLsitckV(3840)
                if event.key == config.lstickKeyDown:
                    await wrapper.moveLsitckV(256)
                if event.key == config.lstickKeyLeft:
                    await wrapper.moveLsitckH(256)
                if event.key == config.lstickKeyRight:
                    await wrapper.moveLsitckH(3840)
                if event.key == config.lstickKeyClick:
                    await wrapper.pushButton('l_stick')
                if event.key == config.rstickKeyClick:
                    await wrapper.pushButton('r_stick')
                if event.key == config.aKey:
                    await wrapper.pushButton('a')
                if event.key == config.bKey:
                    await wrapper.pushButton('b')
                if event.key == config.xKey:
                    await wrapper.pushButton('x')
                if event.key == config.yKey:
                    await wrapper.pushButton('y')
                if event.key == config.dpadUp:
                    await wrapper.pushButton('up')
                if event.key == config.dpadDown:
                    await wrapper.pushButton('down')
                if event.key == config.dpadLeft:
                    await wrapper.pushButton('left')
                if event.key == config.dpadRight:
                    await wrapper.pushButton('right')
                if event.key == config.lKey:
                    await wrapper.pushButton('l')
                if event.key == config.rKey:
                    await wrapper.pushButton('r')
                if event.key == config.zlKey:
                    await wrapper.pushButton('zl')
                if event.key == config.zrKey:
                    await wrapper.pushButton('zr')
                if event.key == config.minusKey:
                    await wrapper.pushButton('minus')
                if event.key == config.plusKey:
                    await wrapper.pushButton('plus')
                if event.key == pygame.K_LALT:
                    alt = True
                if event.key == pygame.K_e:
                    eToggle = True
                if event.key == config.nfcKey:
                    if not nfcKeyOnce:
                        if wrapper.nfcIsEmpty():
                            _loop = asyncio.get_event_loop()
                            Tk().withdraw() # without this a blank window will appear after choosing the
                            filepath = askopenfilename(initialdir="./", title = "Select Amiibo Dump",
                                                        filetypes=(("Binary","*.bin"),("All Files", "*.*")))
                            if not filepath == '' and not filepath == ():
                                with open(filepath, 'rb') as nfcFile:
                                    content = await _loop.run_in_executor(None, nfcFile.read)
                                    await wrapper.setNfc(content)
                        else:
                            await wrapper.setNfc(None)
                        nfcKeyOnce = True
            if event.type == pygame.KEYUP:
                if event.key == config.lstickKeyUp:
                    await wrapper.moveLsitckV(2048)
                if event.key == config.lstickKeyDown:
                    await wrapper.moveLsitckV(2048)
                if event.key == config.lstickKeyLeft:
                    await wrapper.moveLsitckH(2048)
                if event.key == config.lstickKeyRight:
                    await wrapper.moveLsitckH(2048)
                if event.key == config.lstickKeyClick:
                    await wrapper.releaseButton('l_stick')
                if event.key == config.rstickKeyClick:
                    await wrapper.releaseButton('r_stick')
                if event.key == config.aKey:
                    await wrapper.releaseButton('a')
                if event.key == config.bKey:
                    await wrapper.releaseButton('b')
                if event.key == config.xKey:
                    await wrapper.releaseButton('x')
                if event.key == config.yKey:
                    await wrapper.releaseButton('y')
                if event.key == config.lKey:
                    await wrapper.releaseButton('l')
                if event.key == config.dpadUp:
                    await wrapper.releaseButton('up')
                if event.key == config.dpadDown:
                    await wrapper.releaseButton('down')
                if event.key == config.dpadLeft:
                    await wrapper.releaseButton('left')
                if event.key == config.dpadRight:
                    await wrapper.releaseButton('right')
                if event.key == config.rKey:
                    await wrapper.releaseButton('r')
                if event.key == config.zlKey:
                    await wrapper.releaseButton('zl')
                if event.key == config.zrKey:
                    await wrapper.releaseButton('zr')
                if event.key == config.minusKey:
                    await wrapper.releaseButton('minus')
                if event.key == config.plusKey:
                    await wrapper.releaseButton('plus')
                if event.key == pygame.KMOD_ALT:
                    cmToggled = False
                    alt = False
                if event.key == pygame.K_e:
                    cmToggled = False
                    eToggle = False
                if event.key == config.nfcKey:
                    nfcKeyOnce = False
            if event.type == pygame.MOUSEMOTION:
                if config.mouseAsRstick:
                    dx, dy = event.rel
                    """
                    calculating what is worth to send to the switch
                    if the value is too low wont send anything
                    if this check didn't exist then the program would lag a lot
                    """
                    if dx > 50 or dx < -50: 
                        xMoveCheck = True
                        await wrapper.moveRsitckH(maxMinCap((dx * config.rstickSenstivity * -1) + 2048,4095,0))
                    else:
                        if xMoveCheck: # makes sure this happens only once
                            await wrapper.moveRsitckH(2048)
                            xMoveCheck = False
                    if dy > 50 or dy < -50:
                        yMoveCheck = True
                        await wrapper.moveRsitckV(maxMinCap((dy * config.rstickSenstivity) + 2048,4095,0))
                    else:
                        if yMoveCheck:
                            await wrapper.moveRsitckV(2048)
                            yMoveCheck == False
        if alt and eToggle and not cmToggled: 
            catchMouse = not catchMouse
            cmToggled = True
        if catchMouse:
            pygame.mouse.set_pos([100,100])
        gameDisp.fill((255,255,255))
        if wrapper.connected:
            statusText("Connected!")
        if not wrapper.nfcIsEmpty() and not filepath == '':
            nfcText("nfc: "+filepath)
        else:
            nfcText("nfc: None")
        pygame.display.update()
        clock.tick(30)
    pygame.quit()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
