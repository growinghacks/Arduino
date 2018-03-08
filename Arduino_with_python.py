import serial
import pygame

ser = serial.Serial('/dev/rfcomm0', 9600)

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Robot!')
pygame.mouse.set_visible(1)

val = '-'

while val != 'stop':
    events = pygame.event.get()
    for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                        ser.write('a')
                elif event.key == pygame.K_LEFT:
                        ser.write('i')
            elif event.key == pygame.K_RIGHT:
                ser.write('d')
            elif event.key == pygame.K_DOWN:
                ser.write('r')
            elif event.key == pygame.K_ESCAPE:
                    val = 'stop'
        if event.type == pygame.KEYUP:
            ser.write('s')
