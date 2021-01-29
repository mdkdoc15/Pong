import pygame
import random

# Global Vars
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

class Ball:
	def __init__(self):
		self.position = [SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2]
		self.movement = [1,1]
		self.color = WHITE
		self.size = 20

	def start(self):
		self.movement = (random.choice([-1,1]) , random.choice([-1,1] ))
	
	def draw(self, win):
		pygame.draw.circle(win, self.color, [self.position[0],self.position[1]], self.size)
	def update_pos(self):
		self.position[0] = self.position[0] + self.movement[0]*5
		self.position[1] = self.position[1] + self.movement[1]*5
class Paddle:
	def __init__(self, char):
		if char == "L":
			self.position = [25,0]
		else:
			self.position = [860,SCREEN_HEIGHT-100]
		self.color = WHITE

		self.width = 15
		self.height = 100
	
	def update_pos(self, val):
		if val < 0:
			self.position[1] = self.position[1] + 5
		else:
			self.position[1] = self.position[1] - 5
	def draw(self, win):
		pygame.draw.rect(win, self.color, [self.position[0], self.position[1], self.width, self.height])

def draw(win,l_pad, r_pad, ball):
	win.fill(BLACK)
	ball.draw(win)
	l_pad.draw(win)
	r_pad.draw(win)

def main():
	pygame.init()
	clock = pygame.time.Clock()
	
	run = True
	ball = Ball()
	left_paddle = Paddle("L")
	right_paddle = Paddle("R")
	while run:
		clock.tick(30)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					right_paddle.update_pos(1)

		draw(WIN, left_paddle, right_paddle, ball)
		ball.update_pos()
		pygame.display.update()




main()
