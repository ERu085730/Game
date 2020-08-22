#!/usr/bin/env python
#
#
#
#
#

# documentation string of this module
"""
tutorial 01: first blit
"""
# some informational variables
__author__    = "$Author: DR0ID $"
__version__   = "$Revision: 113 $"
__date__      = "$Date: 2007-04-03 18:11:29 +0200 (Di, 03 Apr 2007) $"
__license__   = 'public domain'
__copyright__ = "DR0ID (c) 2007   http://mypage.bluewin.ch/DR0ID"

#----------------------------- actual code --------------------------------

# import the pygame module, so you can use it
import pygame

# define a main function
def main():
    
    # initialize the pygame module
    pygame.init()
    
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("colorkey blit")
    
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((240,180))
    
    # load image (it is in same directory)
    image = pygame.image.load("01_image.png")
    image.set_colorkey((255,0,255))
    image.set_alpha(128)
    bgd_image = pygame.image.load("background.png")
    
    # blit image(s) to screen
    screen.blit(bgd_image,(0,0)) # first background
    
    # instead of blitting the background image you could fill it 
    # (uncomment the next line to do so)
    #screen.fill((255,0,0))
    
    screen.blit(image, (50,50))
    
    # update the screen to make the changes visible (fullscreen update)
    pygame.display.flip()
    
    # define a variable to control the main loop
    running = True
    
    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event if of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
    
    
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
