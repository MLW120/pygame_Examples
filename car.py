import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
#red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('car.png')
Img_width , Img_height = carImg.get_rect().size # you can get size
print(Img_height)
print(Img_width)

def car(x, y,):
	gameDisplay.blit(carImg,(x,y))

x = (display_width * 0.45)
y = (display_height * 0.8)

def update_position(ev):
	global x
	steps = 20
	if ev.key == pygame.K_LEFT:
		x -= steps
		if x < 0:
			x = 0
	if ev.key == pygame.K_RIGHT:
		x += steps
		if x > display_width - 60:
			x = display_width - 60

crashed = False

while not crashed:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True
		print(event)
		if event.type == pygame.KEYDOWN:
			update_position(event)
	

	gameDisplay.fill(white)
	car(x,y)
	
	pygame.display.update()
	clock.tick(60)
	
pygame.quit()

quit()
