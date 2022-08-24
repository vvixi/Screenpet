import pygame
from pygame.locals import *
import time
import math
import random as rand
# Screenpet is a simple virtual pet game made in Python 3 and Pygame.
# Press Left Arrow to skold the pet, Right Arrow feeds the pet.
# The pets mood will decrement slowly.
# Skolding decreases the pets mood, feeding increases its mood.
# Too much skolding will make the pet sad, cranky, then sleepy.
# Too much candy and the pet will become hyper then aggitated.
# The pet starts the game with a varying pastel color skin

# basic setup
width : int = 600
height : int  = 600
pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Virtual Buddy")
colors = [[255,204,230], [230,242,255], [234,255,230], [255,242,230], [234,230,255], [251,230,255], [255, 204, 230]]
rand.shuffle(colors)
my_color = colors.pop()
window.fill((my_color))
fps : int = 16

# game setup
mood : float = 40.0
modifier : int = 10
is_eating : bool = False
eat_time : int = 0
candy = pygame.draw.circle(window, (0, 0, 200), [width/2, 400], 32, 0)
# clamp values of moods to range
def clamp(n, smallest, largest):
	return max(smallest, min(n, largest))

# ranges and corresponding moods
def set_expression(mood):
	if not is_eating:
		if mood >= 90.0:
			aggitated()
		elif mood >= 80.0 and mood < 90.0:
			hyper()
		elif mood >= 70.0 and mood < 80.0:
			laughing()
		elif mood >= 60.0 and mood < 70.0:
			happy()
		elif mood >= 50.0 and mood < 60.0:
			hungry()
		elif mood >= 40.0 and mood < 50.0:
			neutral()
		elif mood >= 30.0 and mood < 40.0:
			bored()
		elif mood >= 20.0 and mood < 30.0:
			cranky()
		elif mood >= 10.0 and mood < 20.0:
			sad()
		elif mood >= 1.0 and mood < 10.0:
			sleepy()

# assorted eyes that the emotions will draw from
def round_eyes():
	if rand.randint(1,12) % 12:
		pygame.draw.circle(window, (0, 0, 0), [150, 250], 30, 0)
		pygame.draw.circle(window, (0, 0, 0), [450, 250], 30, 0)
		spark2 = pygame.draw.circle(window, (255, 255, 255), [450, rand.randrange(238, 240)], 10, 0)
		spark1 = pygame.draw.circle(window, (255, 255, 255), [150, rand.randrange(238, 240)], 10, 0)
	else:
		line_eyes()

def line_eyes():
	# was 250 for eye height
	shake = rand.randrange(240, 250)
	pygame.draw.line(window, (0, 0, 0),[100, shake], [200, shake], 15)
	pygame.draw.line(window, (0, 0, 0),[400, shake], [500, shake], 15)

def squint_eyes():
	#pygame.draw.polygon(window, (255, 255, 255), [[150, 250], [150, 200], [200, 250]])
	shake = [rand.randrange(100, 105), rand.randrange(200, 205), rand.randrange(400, 405), rand.randrange(500, 505)]
	pygame.draw.line(window, (0, 0, 0),[shake[0], 245], [shake[1], 245], 15)
	pygame.draw.line(window, (0, 0, 0),[shake[2], 245], [shake[3], 245], 15)
	pygame.draw.line(window, (0, 0, 0),[shake[0], 220], [shake[1], 245], 15)
	pygame.draw.line(window, (0, 0, 0),[shake[2], 245], [shake[3], 220], 15)

def alert_eyes():
	shake = rand.randrange(2,5)
	pygame.draw.circle(window, (0, 0, 0), [150+shake, 250], 32, 0)
	pygame.draw.circle(window, (0, 0, 0), [450+shake, 250], 32, 0)
	spark2 = pygame.draw.circle(window, (255, 255, 255), [450, rand.randrange(238, 240)], 10, 0)
	spark1 = pygame.draw.circle(window, (255, 255, 255), [150, rand.randrange(238, 240)], 10, 0)

def sleep_eyes():
	risefall = rand.randrange(2,5)
	l1 = pygame.draw.arc(window, (0, 0, 0), (150, 250+risefall, 60, 60), math.radians(180), math.radians(0), width=10)
	l1 = pygame.draw.arc(window, (0, 0, 0), (400, 250+risefall, 60, 60), math.radians(180), math.radians(0), width=10)

clock = pygame.time.Clock()

# assorted emotions the pet will cycle through
def laughing():
	laugh = [rand.randrange(450, 550), rand.randrange(100, 105), rand.randrange(500, 505), rand.randrange(300, 305)]
	mouth = pygame.draw.polygon(window, (255, 0, 0), [[laugh[1], 300], [laugh[2], 300], [300, laugh[0] ]])
	squint_eyes()

def hungry():
	mouth = pygame.draw.ellipse(window, (255, 0, 0), (220, 340, 200, 60))
	#mouth = pygame.draw.circle(window, (255, 0, 0), [300, 380], 30, 0)
	drool()
	round_eyes()

def crying():
	cry = rand.randrange(250, 350)
	lipquiver = rand.randrange(15, 25)
	#mouth = pygame.draw.polygon(window, (255, 0, 0), [[rand.randrange(90,100), bottom], [rand.randrange(490,500), bottom], [300, cry ]])
	mouth = pygame.draw.arc(window, (255, 0, 0), (100, 300, 400, 300), math.radians(0), math.radians(180), width=lipquiver)
	line_eyes()
	tears()

def neutral():
	mouth = pygame.draw.polygon(window, (255, 0, 0), [[100, 380], [500, 380], [300, 480]])
	round_eyes()

def bored():
	mouth = pygame.draw.line(window, (255, 0, 0),[100, 380], [500, 380], 15)
	round_eyes()

def sad():
	corner1 = rand.randrange(30, 35)
	corner2 = rand.randrange(150, 155)
	mouth = pygame.draw.arc(window, (255, 0, 0), (100, 300, 400, 300), math.radians(corner1), math.radians(corner2), width=15)
	#mouth = pygame.draw.polygon(window, (255, 0, 0), [[100, 380], [500, 380], [300, 300 ]])
	if rand.randint(0,12)%6==0:
		line_eyes()
	else:
		crying()

def cranky():
	mouth = pygame.draw.line(window, (255, 0, 0),[200, 380], [400, 380], 60)
	squint_eyes()

def happy():
	mouth = pygame.draw.arc(window, (255, 0, 0), (100, 100, 400, 300), math.radians(210), math.radians(330), width=15)
	round_eyes()

def open():
	mouth = pygame.draw.ellipse(window, (255, 0, 0), (100, 300, 400, 200))
	round_eyes()

def open2():
	mouth = pygame.draw.ellipse(window, (255, 0, 0), (200, 300, 200, 100))
	round_eyes()

def close():
	mouth = pygame.draw.line(window, (255, 0, 0),[100, 380], [500, 380], 25)
	round_eyes()

def sleepy():
	if rand.randrange(1,12) % 2== 0:
		mouth = pygame.draw.circle(window, (255, 0, 0), [width/2, 400], 10, 0)
		time.sleep(.8)
	else:
		mouth = pygame.draw.ellipse(window, (255, 0, 0), (200, 350, 200, 100))
		time.sleep(.8)
	sleep_eyes()

def tears():
	pygame.draw.line(window, (230, 255, 251),[90, 240], [90, 600], 15)
	pygame.draw.line(window, (230, 255, 251),[510, 240], [510, 600], 15)

def drool():
	drop = rand.randrange(400, 450)
	pygame.draw.line(window, (230, 255, 251),[336, 400], [336, drop], 15)

def hyper():
	talk = rand.randrange(300, 550)
	mouth = pygame.draw.polygon(window, (255, 0, 0), [[100, 380], [500, 380], [300, talk ]])
	round_eyes()

def aggitated():
	tremble = rand.randrange(2, 5)
	if rand.randint(1,12) % 2:
		window.fill((my_color))
		alert_eyes()
		l1 = pygame.draw.arc(window, (255, 0, 0), (140, 330, 60, 60), math.radians(180), math.radians(0), width=10)
		l2 = pygame.draw.arc(window, (255, 0, 0), (190, 330, 60, 60), math.radians(360), math.radians(180), width=10)
		l3 = pygame.draw.arc(window, (255, 0, 0), (240, 330, 60, 60), math.radians(180), math.radians(0), width=10)
		l4 = pygame.draw.arc(window, (255, 0, 0), (290, 330, 60, 60), math.radians(360), math.radians(180), width=10)
		l5 = pygame.draw.arc(window, (255, 0, 0), (340, 330, 60, 60), math.radians(180), math.radians(0), width=10)
		l6 = pygame.draw.arc(window, (255, 0, 0), (390, 330, 60, 60), math.radians(360), math.radians(180), width=10)
		time.sleep(.1)

	else:
		window.fill((my_color))
		alert_eyes()
		l1 = pygame.draw.arc(window, (255, 0, 0), (140, 330, 60, 60), math.radians(360), math.radians(180), width=10)
		l2 = pygame.draw.arc(window, (255, 0, 0), (190, 330, 60, 60), math.radians(180), math.radians(360), width=10)
		l3 = pygame.draw.arc(window, (255, 0, 0), (240, 330, 60, 60), math.radians(360), math.radians(180), width=10)
		l4 = pygame.draw.arc(window, (255, 0, 0), (290, 330, 60, 60), math.radians(180), math.radians(360), width=10)
		l5 = pygame.draw.arc(window, (255, 0, 0), (340, 330, 60, 60), math.radians(360), math.radians(180), width=10)
		l6 = pygame.draw.arc(window, (255, 0, 0), (390, 330, 60, 60), math.radians(180), math.radians(360), width=10)
		time.sleep(.1)

def eating():
	global is_eating
	# while eat_time < 10:
	if rand.randint(1,12) % 2 == 0:
		window.fill((my_color))
		open()
		time.sleep(.4)

	else:
		window.fill((my_color))
		open2()
		time.sleep(.4)
	# for i in range(20):
		
	candy = pygame.draw.circle(window, (0, 0, 200), [width/2, 400], 32, 0)
	candysheen = pygame.draw.circle(window, (0, 90, 255), [width/2, 395], 12, 0)


	is_eating = False
	if mood <= 90:
		mod_add()
	eat_time = 0
	return

# modify the pet's mood
def mod_add():
	global mood
	mood = clamp(mood + modifier, 0.0, 100.0)
	return

def mod_sub():
	global mood
	if mood >= 10:
		mood = clamp(mood - modifier, 0.0, 100.0)
	return

# main game loop
while True:
	print(mood)
	clock.tick(fps)
	mood = clamp(mood-(0.05), 0.0, 100.0)
	# mood = clamp(mood-rand.uniform(-0.016, 0.012), 0.0, 100.0)
	pygame.display.update()

	if not is_eating:
		window.fill((my_color))
		set_expression(mood)

	elif is_eating:
		eating()
		candy.move(0, -200)

	pygame.display.update()

	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				mod_sub()
			if event.key == K_RIGHT:
				eating()
				is_eating = True