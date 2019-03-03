import sys
import pygame
import time


pygame.init()

display_width=800
display_height=600

white = (255,255,255)
black = (0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')


gameExit = True

lead_x=display_width/2
lead_y =display_height/2
lead_x_change=0
lead_y_change=0

clock=pygame.time.Clock()

font=pygame.font.SysFont(None,30)

def message_to_screen(msg,color):
    screen_text=font.render(msg,True,color)
    gameDisplay.blit(screen_text,[(display_width/2)-150,display_height/2])

def gameloop():
    global lead_y
    global lead_x
    global lead_x_change
    global lead_y_change
    global gameExit
    while  gameExit:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change=-10
                    lead_y_change=0
                if event.key == pygame.K_RIGHT:
                    lead_x_change=10
                    lead_y_change=0
                if event.key==pygame.K_UP:
                      lead_y_change=-10
                      lead_x_change=0
                if event.key==pygame.K_DOWN:
                    lead_y_change=10
                    lead_x_change=0

        if lead_x>=display_width-20 or lead_x<=10 or lead_y>=display_height-20 or lead_y<=5:

            gameExit=False

        lead_x+=lead_x_change
        lead_y+=lead_y_change

        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay,black,[lead_x,lead_y,10,10])
        pygame.display.update()
        clock.tick(30)

    message_to_screen("You Lose,Better Luck Next time!",red)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()


gameloop()
