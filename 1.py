import pygame
pygame.init()
pygame.display.set_mode((1024,768))

run=True

while run:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
		
pygame.quit()