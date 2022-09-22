import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

#fps
clock = pygame.time.Clock()
fps = 60

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Ban Nhau')

bg_img = pygame.image.load('img/bg.png')

red = (255,0,0)
green = (0,255,0)

def draw_bg():
	screen.blit(bg_img,(0,0))

class Spaceship(pygame.sprite.Sprite):
	def __init__(self, x, y, health):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/spaceship.png')
		self.rect = self.image.get_rect()
		self.rect.center = [x,y]
		self.health_start = health
		self.health_remaining = health
		self.last_shot = pygame.time.get_ticks()
        
        
	def update(self):
		speed = 10
		speed_cooldown = 500

			
           	


		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT] and  self.rect.left > 0:
			self.rect.x -= speed
		if key[pygame.K_RIGHT] and  self.rect.right < SCREEN_WIDTH:
			self.rect.x += speed
		if key[pygame.K_UP]  and self.rect.y > 0:
			self.rect.y -= speed
		if key[pygame.K_DOWN] and self.rect.y < 750:
			self.rect.y += speed


		
		time_now = pygame.time.get_ticks()

		#shoot
		if key[pygame.K_SPACE] and time_now - self.last_shot > speed_cooldown:
			bullet = Bullets(self.rect.centerx,self.rect.top)
			bullet_group.add(bullet)
			self.last_shot = time_now
		pygame.draw.rect(screen,red, (self.rect.x,(self.rect.bottom + 10), self.rect.width,15))
		if self.health_remaining > 0:
			pygame.draw.rect(screen,green, (self.rect.x,(self.rect.bottom + 10), self.rect.width,15))
		
      



       
		
       
            

class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.speed = 10

    def update(self):
        self.rect.y -= 10
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.spritecollide(self,spaceship_group1, True):
        	spaceship.health_remaining -= 1
        	self.kill()

spaceship_group1 = pygame.sprite.Group()
spaceship_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

#create player
spaceship = Spaceship(int(SCREEN_WIDTH / 2), SCREEN_HEIGHT - 100, 5)
spaceship_group.add(spaceship)

spaceship1 = Spaceship(int(SCREEN_WIDTH /2), 100, 5)
spaceship_group1.add(spaceship1)



run = True
while run:
	clock.tick(fps)
	draw_bg()


	spaceship_group.update()
	spaceship_group1.update()
	bullet_group.update()

	spaceship_group.draw(screen)
	spaceship_group1.draw(screen)
	bullet_group.draw(screen)



    
            


    
    

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	pygame.display.update()

pygame.quit()