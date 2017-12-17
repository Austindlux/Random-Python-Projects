import pygame
import sys

def run_game():
	pygame.init()
	screen = pygame.display.set_mode((400,450))
	pygame.display.set_caption('Tic Tac Toe')	
	
	# Creates board and starts hover
	board = create_img()
	hover = Hover(screen)
	game_active = True
	
	peices_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
	peices = []
	player = Player(screen)
	
	while True:
		check_events(hover, peices, screen, player, peices_dict, game_active)
		screen.fill((101, 101, 101))
		player.blitme()
		if game_active:
			screen.blit(board[0], board[1])
			hover.update()
			hover.blitme()
			if peices:
				for i in range(len(peices)):
					peices[i].blitme()
		
		pygame.display.flip()
		
		
def check_events(hover, peices, screen, player, peices_dict, game_active):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				sys.exit()
			if event.key == pygame.K_RIGHT:
				move('right', hover, peices_dict)
			if event.key == pygame.K_LEFT:
				move('left', hover, peices_dict)
			if event.key == pygame.K_UP:
				move('up', hover, peices_dict)
			if event.key == pygame.K_DOWN:
				move('down', hover, peices_dict)
			if event.key == pygame.K_RETURN:
				new_peice(hover, peices, screen, player, peices_dict, game_active)
					
					
def win_message(hover, peices, screen, player, peices_dict, game_active, winner):
	
	if winner == 1:
		player.text = 'Player 1 Wins'
	elif winner == 2:
		player.text = 'Player 2 wins'
	else:
		player.text = 'Game Over'
	player.prep_player()
	player.text_image_rect.centery = player.screen_rect.centery
	while True:
		check_events(hover, peices, screen, player, peices_dict, game_active)
		screen.fill((101, 101, 101))
		player.blitme()
		pygame.display.flip()
		

					
def check_for3(hover, peices, screen, player, peices_dict, game_active):
	# Check Player 1
	if peices_dict[1] == 1 and peices_dict[2] == 1 and peices_dict[3] == 1:
		win_message(hover, peices, screen, player, peices_dict, game_active, 1)
	if peices_dict[4] == 1 and peices_dict[5] == 1 and peices_dict[6] == 1:
		win_message(hover, peices, screen, player, peices_dict, game_active, 1)
	if peices_dict[7] == 1 and peices_dict[8] == 1 and peices_dict[9] == 1:
		win_message(hover, peices, screen, player, peices_dict, game_active, 1)
	if peices_dict[1] == 1 and peices_dict[4] == 1 and peices_dict[7] == 1:
		win_message(hover, peices, screen, player, peices_dict, game_active, 1)
	if peices_dict[2] == 1 and peices_dict[5] == 1 and peices_dict[8] == 1:
		win_message(hover, peices, screen, player, peices_dict, game_active, 1)
	if peices_dict[3] == 1 and peices_dict[6] == 1 and peices_dict[9] == 1:
		win_message(hover, peices, screen, player, peices_dict, game_active, 1)
	if peices_dict[1] == 1 and peices_dict[5] == 1 and peices_dict[9] == 1:
		win_message(hover, peices, screen, player, peices_dict, game_active, 1)
	if peices_dict[3] == 1 and peices_dict[5] == 1 and peices_dict[7] == 1:
		win_message(hover, peices, screen, player, peices_dict, game_active, 1)
		
	# Check Player 2
	if peices_dict[1] == 2 and peices_dict[2] == 2 and peices_dict[3] == 2:
		win_message(hover, peices, screen, player, peices_dict, game_active, 2)
	if peices_dict[4] == 2 and peices_dict[5] == 2 and peices_dict[6] == 2:
		win_message(hover, peices, screen, player, peices_dict, game_active, 2)
	if peices_dict[7] == 2 and peices_dict[8] == 2 and peices_dict[9] == 2:
		win_message(hover, peices, screen, player, peices_dict, game_active, 2)
	if peices_dict[1] == 2 and peices_dict[4] == 2 and peices_dict[7] == 2:
		win_message(hover, peices, screen, player, peices_dict, game_active, 2)
	if peices_dict[2] == 2 and peices_dict[5] == 2 and peices_dict[8] == 2:
		win_message(hover, peices, screen, player, peices_dict, game_active, 2)
	if peices_dict[3] == 2 and peices_dict[6] == 2 and peices_dict[9] == 2:
		win_message(hover, peices, screen, player, peices_dict, game_active, 2)
	if peices_dict[1] == 2 and peices_dict[5] == 2 and peices_dict[9] == 2:
		win_message(hover, peices, screen, player, peices_dict, game_active, 2)
	if peices_dict[3] == 2 and peices_dict[5] == 2 and peices_dict[7] == 2:
		win_message(hover, peices, screen, player, peices_dict, game_active, 2)
		
		
def move(key, hover, peices_dict):
	if key == 'up':
		if hover.hover_pos not in (1, 2, 3) and peices_dict[hover.hover_pos - 3] == 0:
			hover.hover_pos -= 3
		elif hover.hover_pos not in (1, 2, 3, 4, 5, 6) and peices_dict[hover.hover_pos - 6] == 0:
			hover.hover_pos -= 6
		else:
			move('next-', hover, peices_dict)
			
	if key == 'down':	
		if hover.hover_pos not in (7, 8, 9) and peices_dict[hover.hover_pos + 3] == 0:
			hover.hover_pos += 3
		elif hover.hover_pos not in (4, 5, 6, 7, 8, 9) and peices_dict[hover.hover_pos + 6] == 0:
			hover.hover_pos += 6
		else:
			move('next+', hover, peices_dict)
			
	if key == 'right':
		if hover.hover_pos not in (3, 6, 9) and peices_dict[hover.hover_pos + 1] == 0:
			hover.hover_pos += 1
		elif hover.hover_pos not in (2, 3, 5, 6, 8, 9) and peices_dict[hover.hover_pos + 2] == 0:
			hover.hover_pos += 2
		else:
			move('next+', hover, peices_dict)
	
	if key == 'left':
		if hover.hover_pos not in (1, 4, 7) and peices_dict[hover.hover_pos - 1] == 0:
			hover.hover_pos -= 1
		elif hover.hover_pos not in (1, 2, 4, 5, 7, 8) and peices_dict[hover.hover_pos - 2] == 0:
			hover.hover_pos -= 2
		else:
			move('next-', hover, peices_dict)
	
	if key == 'next+':
		for k in peices_dict:
			if k + hover.hover_pos > 9:
				break
			if peices_dict[k + hover.hover_pos] == 0:
				hover.hover_pos += k
				break
				
	if key == 'next-':
		for k in peices_dict:
			if hover.hover_pos - k < 1:
				break
			if peices_dict[hover.hover_pos - k] == 0:
				hover.hover_pos -= k
				break
			
			

			
						
def new_peice(hover, peices, screen, player, peices_dict, game_active):
	# Place peice on screen
	new_peice = Peice(screen, hover, player)
	peices.append(new_peice)
	if player.text == 'Player 1':
		peices_dict[hover.hover_pos] = 1
	else: 
		peices_dict[hover.hover_pos] = 2
	
	# Changes hover_pos
	if 0 not in peices_dict.values():
		win_message(hover, peices, screen, player, peices_dict, game_active, 3)
	else:
		move('next+', hover, peices_dict)
		if peices_dict[hover.hover_pos] != 0:
			move('next-', hover, peices_dict)
				
			
	# Switch from player 1 to 2 or visa versa.
	if player.text == 'Player 1':
		player.text = 'Player 2'
	else:
		player.text = 'Player 1'
	player.prep_player()
	
	# Check if anyone won
	check_for3(hover, peices, screen, player, peices_dict, game_active)
				
	
def create_img():
	img = pygame.image.load('ttt_board.png')
	img_rect = img.get_rect()
	img_rect.x = 1
	img_rect.y = 50
	return (img, img_rect)
	

class Hover():
	def __init__(self, screen):
		self.screen = screen
		self.vertical = 0
		self.horizontal = 0
		self.color = (179, 179, 179)
		self.hover_pos = 1
		
		self.rect = pygame.Rect(0, 50, 114, 119)
		
	def update(self):
		if self.hover_pos == 1:
			self.rect = pygame.Rect(0, 50, 114, 119)
		if self.hover_pos == 2:
			self.rect = pygame.Rect(129, 50, 134, 119)
		if self.hover_pos == 3:
			self.rect = pygame.Rect(277, 50, 124, 119)
		if self.hover_pos == 4:
			self.rect = pygame.Rect(0, 182, 114, 137)
		if self.hover_pos == 5:
			self.rect = pygame.Rect(129, 182, 134, 137)
		if self.hover_pos == 6:
			self.rect = pygame.Rect(277, 182, 123, 137)
		if self.hover_pos == 7:
			self.rect = pygame.Rect(0, 331, 114, 119)
		if self.hover_pos == 8:
			self.rect = pygame.Rect(129, 331, 134, 119)
		if self.hover_pos == 9:
			self.rect = pygame.Rect(277, 331, 123, 119)
		
	def blitme(self):
		pygame.draw.rect(self.screen, self.color, self.rect)

class Peice():
	def __init__(self, screen, hover, player):
		self.screen = screen 
		if player.text == 'Player 1':
			self.img = pygame.image.load('x.png')
			self.img = pygame.transform.scale(self.img, (85, 85))
			self.img_rect = self.img.get_rect()
			self.img_rect.x = hover.rect.x + 10
			self.img_rect.y = hover.rect.y + 15
		else:
			self.img = pygame.image.load('o.jpg')
			self.img = pygame.transform.scale(self.img, (100, 100))
			self.img_rect = self.img.get_rect()
			self.img_rect.x = hover.rect.x + 10
			self.img_rect.y = hover.rect.y + 10
			
	def blitme(self):
		self.screen.blit(self.img, self.img_rect)
	
	
class Player():
	def __init__(self, screen):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.text_color = (0, 0, 0)
		self.font = pygame.font.SysFont(None, 55)
		self.text = 'Player 1'
		
		self.prep_player()
		
	def prep_player(self):
		self.text_image = self.font.render(self.text, True, self.text_color, (101, 101, 101))
		self.text_image_rect = self.text_image.get_rect()
		self.text_image_rect.centerx = self.screen_rect.centerx
		self.text_image_rect.y = 4

	def blitme(self):
		self.screen.blit(self.text_image, self.text_image_rect)
	

run_game()
