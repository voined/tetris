import pygame
import random
import time
pygame.init()
pygame.font.init() 

pygame.display.set_caption('Tetris')

clock = pygame.time.Clock()

screen_width = 350
screen_height = 700

bg_color = (0, 0, 0)

win = pygame.display.set_mode((screen_width, screen_height))

pygame.mixer.music.load('theme_song.mp3')
pygame.mixer.music.play(-1)



class blocks(object):
	def __init__(self, x, y):
		self.x = x * (screen_height/20)
		self.y = y * (screen_height/20)

		self.lowestblock = 0
		self.rightmostblock = 0
		self.leftmostblock = 0

		self.lowerblocks = []
		self.upperblocks = []
		self.rightblocks = []
		self.leftblocks = []

		self.blocksize = (screen_height/20)

		self.downforce = self.blocksize

		self.type = 0
		self.number = 0
		self.moving = True
		self.color = 0
		self.ispressed = False

		self.allowright = True
		self.allowleft = True

		self.rightleftvel = self.blocksize






	def controls(self):
		KEYS = pygame.key.get_pressed()
		global theblocks
		global NEXTBLOCK






		for block1 in theblocks:
			if block1.number != self.number and block.moving == True:

				if self.x + self.rightmostblock*self.blocksize >= block1.x + block1.leftmostblock*block1.blocksize and self.x + self.leftmostblock*self.blocksize <= block1.x + block1.rightmostblock*block1.blocksize:
					#THE BLOCK IS THE ONE IN MOTION, THE BLOCK1 IS THE STABLE

					for i in range(len(block1.upperblocks)):
						for j in range(len(self.lowerblocks)):

							if self.x + self.lowerblocks[j][0]*self.blocksize == block1.x + block1.upperblocks[i][0]*block1.blocksize:
								if self.y + self.blocksize + self.lowerblocks[j][1]*self.blocksize == block1.y + block1.upperblocks[i][1]*block1.blocksize:

									block1.moving = False
									self.moving = False


									NEXTBLOCK = True


									





				else:
					c = 0
					for i in range(len(block1.rightblocks)):
						for j in range(len(self.rightblocks)):

							if self.y + self.lowestblock*self.blocksize >= block1.y and self.y <= block1.y + block1.lowestblock*block1.blocksize:
								print(c)
								c+=1
								if self.x + self.rightmostblock*self.blocksize + self.blocksize == block1.x + block1.leftmostblock*block.blocksize:
									
									
										
				
									self.allowright = False
									
									

								else:
									self.allowright = True
									


				


								if self.x + self.leftmostblock*self.blocksize - self.blocksize == block1.x + block1.rightmostblock*block1.blocksize:
									
									self.allowleft = False

									

								else:
									self.allowleft = True
									




					
		if KEYS[pygame.K_RIGHT] and not(self.ispressed):
			if self.allowright:
				self.x += self.rightleftvel
				self.ispressed = True

	
		if KEYS[pygame.K_LEFT] and not(self.ispressed):
			if self.allowleft:
				self.x -= self.rightleftvel
				self.ispressed = True

		if not(KEYS[pygame.K_RIGHT]) and not(KEYS[pygame.K_LEFT]):
			self.ispressed = False





					



	def gravity(self):
		if self.y + self.blocksize < screen_height - self.lowestblock * self.blocksize and self.moving:
			self.y += self.downforce


	def allownext(self):
		global NEXTBLOCK
		global block
		if self.y + self.blocksize >= screen_height - self.lowestblock * self.blocksize:
			NEXTBLOCK = True






	def square(self):

		pygame.draw.rect(win, self.color, (self.x, self.y, self.blocksize, self.blocksize))
		pygame.draw.rect(win, self.color, (self.x + self.blocksize, self.y, self.blocksize, self.blocksize))
		pygame.draw.rect(win, self.color, (self.x, self.y + self.blocksize, self.blocksize, self.blocksize))
		pygame.draw.rect(win, self.color, (self.x + self.blocksize, self.y + self.blocksize, self.blocksize, self.blocksize))
		self.lowestblock = 1
		self.rightmostblock = 1
		self.leftmostblock = 0
		

		self.upperblocks.append((0, 0))
		self.upperblocks.append((1, 0))

		self.lowerblocks.append((0, 1))
		self.lowerblocks.append((1, 1))

		self.rightblocks.append((1, 0))
		self.rightblocks.append((1, 1))

		self.leftblocks.append((0, 0))
		self.leftblocks.append((0, 1))


		#0 to 8 range for x
		#top left block reference point



	def tshape(self):

		pygame.draw.rect(win, self.color, (self.x, self.y, self.blocksize, self.blocksize))
		pygame.draw.rect(win, self.color, (self.x, self.y + self.blocksize, self.blocksize, self.blocksize))
		pygame.draw.rect(win, self.color, (self.x + self.blocksize, self.y + self.blocksize, self.blocksize, self.blocksize))
		pygame.draw.rect(win, self.color, (self.x - self.blocksize, self.y + self.blocksize, self.blocksize, self.blocksize))
		self.lowestblock = 1
		self.rightmostblock = 1
		self.leftmostblock = -1	


		self.upperblocks.append((-1, 1))
		self.upperblocks.append((0, 0))
		self.upperblocks.append((1, 1))

		self.lowerblocks.append((-1, 1))
		self.lowerblocks.append((0, 1))
		self.lowerblocks.append((1, 1))

		self.rightblocks.append((0, 0))
		self.rightblocks.append((1, 1))

		self.leftblocks.append((0, 0))
		self.leftblocks.append((-1, 1))

		#0 to 7 range for x
		#tip block reference point



	def lshape(self):

		pygame.draw.rect(win, self.color, (self.x, self.y, self.blocksize, self.blocksize))
		pygame.draw.rect(win, self.color, (self.x, self.y + self.blocksize, self.blocksize, self.blocksize))
		pygame.draw.rect(win, self.color, (self.x + self.blocksize, self.y + self.blocksize, self.blocksize, self.blocksize))
		pygame.draw.rect(win, self.color, (self.x + 2*self.blocksize, self.y + self.blocksize, self.blocksize, self.blocksize))
		self.lowestblock = 1
		self.rightmostblock = 2
		self.leftmostblock = 0		
		

		self.upperblocks.append((0, 0))
		self.upperblocks.append((1, 1))
		self.upperblocks.append((2, 1))

		self.lowerblocks.append((0, 1))
		self.lowerblocks.append((1, 1))
		self.lowerblocks.append((2, 1))

		self.rightblocks.append((0, 0))
		self.rightblocks.append((2, 1))

		self.leftblocks.append((0, 0))
		self.leftblocks.append((0, 1))




	def ishape(self):

		pygame.draw.rect(win, self.color, (self.x, self.y, self.blocksize, self.blocksize))
		pygame.draw.rect(win, self.color, (self.x, self.y + self.blocksize, self.blocksize, self.blocksize))
		pygame.draw.rect(win, self.color, (self.x, self.y + 2*self.blocksize, self.blocksize, self.blocksize))
		pygame.draw.rect(win, self.color, (self.x, self.y + 3*self.blocksize, self.blocksize, self.blocksize))
		self.lowestblock = 3
		self.rightmostblock = 0
		self.leftmostblock = 0		


		self.upperblocks.append((0, 0))

		self.lowerblocks.append((0, 3))

		self.rightblocks.append((0, 0))
		self.rightblocks.append((0, 1))
		self.rightblocks.append((0, 2))
		self.rightblocks.append((0, 3))

		self.leftblocks.append((0, 0))
		self.leftblocks.append((0, 1))
		self.leftblocks.append((0, 2))
		self.leftblocks.append((0, 3))






	def zshape(self):

		pygame.draw.rect(win, self.color, (self.x, self.y, self.blocksize, self.blocksize))
		pygame.draw.rect(win, self.color, (self.x + self.blocksize, self.y, self.blocksize, self.blocksize))
		pygame.draw.rect(win, self.color, (self.x + self.blocksize, self.y + self.blocksize, self.blocksize, self.blocksize))
		pygame.draw.rect(win, self.color, (self.x + 2*self.blocksize, self.y + self.blocksize, self.blocksize, self.blocksize))
		self.lowestblock = 1
		self.rightmostblock = 2
		self.leftmostblock = 0

		
		self.upperblocks.append((0, 0))
		self.upperblocks.append((1, 0))
		self.upperblocks.append((2, 1))

		self.lowerblocks.append((0, 0))
		self.lowerblocks.append((1, 1))
		self.lowerblocks.append((2, 1))

		self.rightblocks.append((1, 0))
		self.rightblocks.append((2, 1))

		self.leftblocks.append((0, 0))
		self.leftblocks.append((1, 1))






NEXTBLOCK = True
randomblock = 0
block = 0
blocknumber = 1
theblocks = []
blockcolor = 0
gameover_font = pygame.font.SysFont('8-Bit-Madness', 50)
score_font = pygame.font.SysFont('8-Bit-Madness', 30)
yourscore_font = pygame.font.SysFont('8-Bit-Madness', 40)
score = 0





def refreshwindow():
	global NEXTBLOCK
	global randomblock
	global block
	global theblocks
	global blocknumber
	global blockcolor
	global run
	global score
	global gameover_font
	global yourscore_font



	pygame.draw.rect(win, bg_color, (0, 0, screen_width, screen_height))




		

	if NEXTBLOCK:

		blockcolor = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
		
		randomblock = random.randint(1, 5)


		if randomblock == 1:
			block = blocks(random.randint(0, 8), -2) #square
		elif randomblock == 2:
			block = blocks(random.randint(1, 7), -2) #t
		elif randomblock == 3:
			block = blocks(random.randint(0, 7), -2) #l
		elif randomblock == 4:
			block = blocks(random.randint(0, 9), -3) #i
		elif randomblock == 5:
			block = blocks(random.randint(0, 7), -2) #z


		block.type = randomblock
		block.number = blocknumber
		block.color = blockcolor

		blocknumber += 1

		theblocks.append(block)






		NEXTBLOCK = False















	for block in theblocks:
		if block.type == 1:
			block.square()
			block.gravity()

		elif block.type == 2:
			block.tshape()
			block.gravity()

		elif block.type == 3:
			block.lshape()
			block.gravity()

		elif block.type == 4:
			block.ishape()
			block.gravity()

		elif block.type == 5:
			block.zshape()
			block.gravity()


		if block.number == len(theblocks) and block.moving == True:
			block.allownext()
			block.controls()








	if block.y <= 0 and block.moving == False:


		gameover_text = gameover_font.render('GAME OVER', False, (255, 255, 255))
		yourscore_text = yourscore_font.render('YOUR SCORE: ' + str(score), False, (255, 255, 255))

		win.blit(gameover_text,(80,350))
		win.blit(yourscore_text, (70, 400))

		NEXTBLOCK = False

		KEYS = pygame.key.get_pressed()
		if KEYS[pygame.K_r]:
			NEXTBLOCK = True
			theblocks = []
			blocknumber = 1
			score += 1




	score = len(theblocks) - 1

	score_text = score_font.render('SCORE : ' + str(score), False, (255, 255, 255))

	win.blit(score_text, (235, 20))


		

















	pygame.display.update()






run = True
while run:

	clock.tick(10)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False





	refreshwindow()





pygame.quit()