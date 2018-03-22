import ui
from scene import *
import requests
import time
import numpy as np
import matplotlib.path as mpath
server_ip='http://172.20.10.6:5000/'

b=[[[0.0, 7.071, 0], [0.707, 6.364, 0], [1.414, 5.657, 1], [2.121, 4.95, 1], [2.828, 4.243, 1], [3.536, 3.536, 0], [4.243, 2.828, 2], [4.95, 2.121, 2], [5.657, 1.414, 2], [6.364, 0.707, 2], [7.071, 0.0, 2]], [[0.707, 7.778, 0], [1.414, 7.071, 1], [2.121, 6.364, 1], [2.828, 5.657, 1], [3.536, 4.95, 1], [4.243, 4.243, 0], [4.95, 3.536, 2], [5.657, 2.828, 2], [6.364, 2.121, 2], [7.071, 1.414, 2], [7.778, 0.707, 2]], [[1.414, 8.485, 1], [2.121, 7.778, 1], [2.828, 7.071, 1], [3.536, 6.364, 1], [4.243, 5.657, 1], [4.95, 4.95, 0], [5.657, 4.243, 2], [6.364, 3.536, 2], [7.071, 2.828, 2], [7.778, 2.121, 2], [8.485, 1.414, 2]], [[2.121, 9.192, 1], [2.828, 8.485, 1], [3.536, 7.778, 1], [4.243, 7.071, 1], [4.95, 6.364, 1], [5.657, 5.657, 0], [6.364, 4.95, 2], [7.071, 4.243, 2], [7.778, 3.536, 2], [8.485, 2.828, 2], [9.192, 2.121, 2]], [[2.828, 9.899, 1], [3.536, 9.192, 1], [4.243, 8.485, 1], [4.95, 7.778, 1], [5.657, 7.071, 1], [6.364, 6.364, 0], [7.071, 5.657, 2], [7.778, 4.95, 2], [8.485, 4.243, 2], [9.192, 3.536, 2], [9.899, 2.828, 2]], [[3.536, 10.607, 1], [4.243, 9.899, 1], [4.95, 9.192, 1], [5.657, 8.485, 1], [6.364, 7.778, 1], [7.071, 7.071, 0], [7.778, 6.364, 2], [8.485, 5.657, 2], [9.192, 4.95, 2], [9.899, 4.243, 2], [10.607, 3.536, 2]], [[4.243, 11.314, 1], [4.95, 10.607, 1], [5.657, 9.899, 1], [6.364, 9.192, 1], [7.071, 8.485, 1], [7.778, 7.778, 0], [8.485, 7.071, 2], [9.192, 6.364, 2], [9.899, 5.657, 2], [10.607, 4.95, 2], [11.314, 4.243, 2]], [[4.95, 12.021, 1], [5.657, 11.314, 1], [6.364, 10.607, 1], [7.071, 9.899, 1], [7.778, 9.192, 1], [8.485, 8.485, 0], [9.192, 7.778, 2], [9.899, 7.071, 2], [10.607, 6.364, 2], [11.314, 5.657, 2], [12.021, 4.95, 2]], [[5.657, 12.728, 1], [6.364, 12.021, 1], [7.071, 11.314, 1], [7.778, 10.607, 1], [8.485, 9.899, 1], [9.192, 9.192, 0], [9.899, 8.485, 2], [10.607, 7.778, 2], [11.314, 7.071, 2], [12.021, 6.364, 2], [12.728, 5.657, 2]], [[6.364, 13.435, 0], [7.071, 12.728, 1], [7.778, 12.021, 1], [8.485, 11.314, 1], [9.192, 10.607, 1], [9.899, 9.899, 0], [10.607, 9.192, 2], [11.314, 8.485, 2], [12.021, 7.778, 2], [12.728, 7.071, 2], [13.435, 6.364, 2]], [[7.071, 14.142, 0], [7.778, 13.435, 0], [8.485, 12.728, 1], [9.192, 12.021, 1], [9.899, 11.314, 1], [10.607, 10.607, 0], [11.314, 9.899, 2], [12.021, 9.192, 2], [12.728, 8.485, 2], [13.435, 7.778, 2], [14.142, 7.071, 2]]]

c=[[[0.0, 7.071, 0], [0.707, 6.364, 0], [1.414, 5.657, 1], [2.121, 4.95, 1], [2.828, 4.243, 1], [3.536, 3.536, 1], [4.243, 2.828, 2], [4.95, 2.121, 2], [5.657, 1.414, 2], [6.364, 0.707, 0], [7.071, 0.0, 0]], [[0.707, 7.778, 0], [1.414, 7.071, 1], [2.121, 6.364, 1], [2.828, 5.657, 1], [3.536, 4.95, 1], [4.243, 4.243, 1], [4.95, 3.536, 2], [5.657, 2.828, 2], [6.364, 2.121, 2], [7.071, 1.414, 2], [7.778, 0.707, 0]], [[1.414, 8.485, 1], [2.121, 7.778, 1], [2.828, 7.071, 1], [3.536, 6.364, 1], [4.243, 5.657, 1], [4.95, 4.95, 1], [5.657, 4.243, 2], [6.364, 3.536, 2], [7.071, 2.828, 2], [7.778, 2.121, 2], [8.485, 1.414, 2]], [[2.121, 9.192, 1], [2.828, 8.485, 1], [3.536, 7.778, 1], [4.243, 7.071, 1], [4.95, 6.364, 1], [5.657, 5.657, 1], [6.364, 4.95, 2], [7.071, 4.243, 2], [7.778, 3.536, 2], [8.485, 2.828, 2], [9.192, 2.121, 2]], [[2.828, 9.899, 1], [3.536, 9.192, 1], [4.243, 8.485, 1], [4.95, 7.778, 1], [5.657, 7.071, 1], [6.364, 6.364, 1], [7.071, 5.657, 2], [7.778, 4.95, 2], [8.485, 4.243, 2], [9.192, 3.536, 2], [9.899, 2.828, 2]], [[3.536, 10.607, 1], [4.243, 9.899, 1], [4.95, 9.192, 1], [5.657, 8.485, 1], [6.364, 7.778, 1], [7.071, 7.071, 1], [7.778, 6.364, 2], [8.485, 5.657, 2], [9.192, 4.95, 2], [9.899, 4.243, 2], [10.607, 3.536, 2]], [[4.243, 11.314, 1], [4.95, 10.607, 1], [5.657, 9.899, 1], [6.364, 9.192, 1], [7.071, 8.485, 1], [7.778, 7.778, 1], [8.485, 7.071, 2], [9.192, 6.364, 2], [9.899, 5.657, 2], [10.607, 4.95, 2], [11.314, 4.243, 2]], [[4.95, 12.021, 1], [5.657, 11.314, 1], [6.364, 10.607, 1], [7.071, 9.899, 1], [7.778, 9.192, 1], [8.485, 8.485, 1], [9.192, 7.778, 2], [9.899, 7.071, 2], [10.607, 6.364, 2], [11.314, 5.657, 2], [12.021, 4.95, 2]], [[5.657, 12.728, 1], [6.364, 12.021, 1], [7.071, 11.314, 1], [7.778, 10.607, 1], [8.485, 9.899, 1], [9.192, 9.192, 1], [9.899, 8.485, 2], [10.607, 7.778, 2], [11.314, 7.071, 2], [12.021, 6.364, 2], [12.728, 5.657, 2]], [[6.364, 13.435, 0], [7.071, 12.728, 1], [7.778, 12.021, 1], [8.485, 11.314, 1], [9.192, 10.607, 1], [9.899, 9.899, 1], [10.607, 9.192, 2], [11.314, 8.485, 2], [12.021, 7.778, 2], [12.728, 7.071, 2], [13.435, 6.364, 0]], [[7.071, 14.142, 0], [7.778, 13.435, 0], [8.485, 12.728, 1], [9.192, 12.021, 1], [9.899, 11.314, 1], [10.607, 10.607, 1], [11.314, 9.899, 2], [12.021, 9.192, 2], [12.728, 8.485, 2], [13.435, 7.778, 0], [14.142, 7.071, 0]]]

class game_scene(Scene):
	def setup(self):
		self.tile_dict = {}
		self.background_color = 'black'
		self.possible_moves = []
		self.active_piece = None
		self.active_player = False
		self.move_tiles_active = False
		self.move_tiles_list = []
		self.update_counter = 0
		for x in range(11):
			for y in range(11):
				if c[x][y][2]>0:
					self.tile_dict[(x,y)]=(b[x][y][0] * 41, b[x][y][1]*27+5)
					self.tile = SpriteNode('tile.png', position=(b[x][y][0] * 41, b[x][y][1]*27+5), scale=.7)
					self.add_child(self.tile)
		self.board = self.get_game_board()
		self.playerid = int(self.get_player_id())
		self.move_number = 0
		self.move_icon = SpriteNode('sprites/icons/move_icon.png', position=(530, 380))
		self.attack_icon = SpriteNode('sprites/icons/attack_icon.png', position=(530+45, 380))
		self.orient_icon = SpriteNode('sprites/icons/orient_icon.png', position=(530+45*2, 380))
		self.wait_icon = SpriteNode('sprites/icons/wait_icon.png', position=(530+45*3, 380))
		self.surrender_icon = SpriteNode('sprites/icons/french_flag.png', position=(530+45*4, 380))
		self.x_y = LabelNode('x, y', font = ('Helvetica', 14), position = (700, 250), color = 'white')
		self.add_child(self.attack_icon)
		self.add_child(self.move_icon)
		self.add_child(self.orient_icon)
		self.add_child(self.wait_icon)
		self.add_child(self.surrender_icon)
		self.add_child(self.x_y)
		self.sprite_info_dict={
		'k':['knight',1,.7, 3],
		's':['scout',1, .7, 4],
		'c':['cleric',1, .7, 3],
		'fg':['fgolem',1, .6, 2],
		'mg':['mgolem',1, .6, 6],
		'sg':['sgolem',1, .7, 2],
		'f':['furgon',1, .7, 3],
		'd':['dragon',2, .5, 4],
		'br':['brider',1, .5, 4]
		}
		
		self.z =[
		[9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
		[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
		[7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
		[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
		[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
		[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
		[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
		[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
		[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
		[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
		[0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
		self.draw_board()
	
	def draw_board(self):
		self.unit_dict={}
		
		for x in range(11):
			for y in range(11):
				if self.board[x][y] is not 0:
					sprite_name = "sprites/%s/%s_%s_%s.png"%(self.sprite_info_dict[self.board[x][y][1]][0],self.sprite_info_dict[self.board[x][y][1]][0], self.board[x][y][0], self.board[x][y][2])
					self.unit_dict[(x,y)]=SpriteNode(sprite_name, position=(b[x][y][0]*41+3, b[x][y][1]*27-5), scale = self.sprite_info_dict[self.board[x][y][1]][2])
					self.unit_dict[(x,y)].anchor_point = (0.5,0)
					self.unit_dict[(x,y)].z_position = self.z[x][y]
					self.add_child(self.unit_dict[(x,y)])
					
	def get_tile_index(self, x,y):	
		for ind, pos in self.tile_dict.items():
			pt1 = [pos[0], pos[1]+self.tile.size[1]/2] 
			pt2 = [pos[0]+self.tile.size[0]/2, pos[1]]
			pt3 = [pos[0], pos[1]-self.tile.size[1]/2]
			pt4 = [pos[0]-self.tile.size[0]/2, pos[1]]
			tile_path = mpath.Path(np.array([[pt1[0],pt1[1]],
													 [pt2[0],pt2[1]],
													 [pt3[0],pt3[1]],
													 [pt4[0],pt4[1]]]))
			if tile_path.contains_point((x,y)): 
				px, py = ind
				return pos, px, py
		return None				
	def get_player_id(self):
		r = requests.get(server_ip+'get_player_id',cookies=client.login_request.cookies)
		return eval(r.content.decode('utf-8'))
		
	def get_game_board(self):
		r = requests.get(server_ip+'get_board_state',cookies=client.login_request.cookies)
		# print("decoded", r.content.decode('utf-8'))
		return eval(r.content.decode('utf-8'))
	
	def process_move(self, move):
		if move[0] == "server":
			if move[2] == 'switch' and move[1] == self.playerid:
				self.active_player = True
				self.move_unused = True
				self.attack_unused = True
				self.move_action = True
				self.moved_unit = None
				
			if move[2] == 'block':
				#update_board
				#self.animate_attack
				pass
			if move[2] == 'endgame':
				pass
		if move[1] == "o":
			#self.animate_orientation()
			#update_board
			pass
		if move[1] == "m":
			#self.animate_move()
			#update_board
			pass
	def send_move(self, move):
		r = requests.post(server_ip+'post_moves', data ={'moves': str(move)}, cookies=client.login_request.cookies)
			
		
	def check_moves(self):
		r = requests.get(server_ip+'get_game_moves',cookies=client.login_request.cookies)
		move_lists = eval(r.content.decode('utf-8'))
		
		if self.move_number == len(move_lists):
			pass #do nothing everything is updated
		else:
			self.process_move(move_lists[self.move_number])
			self.move_number +=1
	def show_attack_tiles(self, attack_range, attack_type, x, y):
		pass
	def show_movement_tiles(self, r, x, y):
		self.active_piece_movement_dict={(x,y):[(0,0)]}
		self.a_m_list =[(x,y)]
		self.move_tiles_active = True
		self.new_m_list = []
		while r>0: 
			r-=1
			while len(self.a_m_list)>0 :
				key = self.a_m_list.pop()
				for k in [(key[0] +1, key[1]) , (key[0], key[1] -1) , (key[0] -1, key[1]), (key[0] , key[1] +1)]:
					if 0<=(k[0])<=10 and 0<=(k[1])<=10:
						_, _, is_tile = c[k[0]][k[1]]
						if is_tile is not 0:
							if self.board[k[0]][k[1]] == 0:
								movable=True
								empty = True
							elif int(self.board[k[0]][k[1]][0]) == int(self.playerid):
								movable=True
								empty = False
							else:
								movable = False
								empty = False
								
							if k not in self.active_piece_movement_dict:
								if movable:
									self.new_m_list.append(k)
									new_path = self.active_piece_movement_dict[key]
									new_path.append(k)
									self.active_piece_movement_dict[k] = new_path
								if empty:
									self.possible_moves.append(k)
									self.tile = SpriteNode('move_tile.png', position=(b[k[0]][k[1]][0] * 41, b[k[0]][k[1]][1]*27+5), scale=.7)
									self.move_tiles_list.append(self.tile)
									self.add_child(self.tile)
			self.a_m_list = self.new_m_list.copy()
	def update(self):
		self.update_counter+=1
		if self.update_counter % 60 == 0:
			self.check_moves()
			self.update_counter = 0
	def change_board(self, move):
		if move[0] == 'm':
			temp = self.board[move[1][0]][move[1][1]]
			self.board[move[1][0]][move[1][1]] = self.board[move[2][0]][move[2][1]]
			self.board[move[2][0]][move[2][1]] = temp
	def touch_began(self, touch):
		x, y = touch.location
		
		if self.move_tiles_active:
			self.move_tiles_active = False
			for mtile in self.move_tiles_list:
				mtile.remove_from_parent()
			self.move_tiles_list = [] 
			p = self.get_tile_index(x,y)
			if p:
				pos, ix, iy = p
				self.x_y.text=str(ix)+" "+ str(iy)
				if (ix,iy) in self.possible_moves:
					self.active_piece.position = (pos[0]+4,pos[1]-10)
					self.active_piece.z_position=self.z[ix][iy]
					self.possible_moves = []
					print("desitation", (ix, iy))
					self.change_board(['m', self.move_unit_origin, [ix,iy]])
					self.send_move([self.playerid, 'move', self.move_unit_origin, [ix,iy]])
					self.move_unused = False
					self.moved_unit = [ix, iy]
			self.active_piece = None			
		elif self.active_player and self.active_piece is None:
			for unit_pos, sprite in self.unit_dict.items():
				xmin = sprite.position.x-sprite.size[0]/2
				xmax = sprite.position.x+sprite.size[0]/2
				ymin = sprite.position.y
				ymax = sprite.position.y +sprite.size[1]
				if  xmin <x< xmax and ymin<y<ymax:
					self.original_e_index = self.get_tile_index(sprite.position.x,sprite.position.y)[1:3]
					u1, u2 = self.original_e_index
					print("origin unit", (u1, u2)) #show unit infographics		
					if self.board[u1][u2] is not 0:
						if int(self.board[u1][u2][0])==self.playerid:
							if self.move_unused and self.move_action:
								unit_key = self.board[u1][u2][1]
								movement_range =self.sprite_info_dict[unit_key][3]
								self.show_movement_tiles(movement_range, u1, u2)
								self.active_piece = sprite
								self.move_unit_origin = [u1,u2]
								self.attack_action = True
							elif self.attack_action and ([u1, u2] == self.moved_unit or self.moved_unit is None):
								attack_range = 3
								attack_type = 'p'
								self.show_attack_tiles(attack_range, attack_type, u1, u2)
								print("attack available")
						else:
							pass
							#print("opponent's piece")
						self.active_any_piece = sprite
	def touch_moved(self,touch):
		pass	
class login(Scene):
	def setup(self):
		self.tile_dict = {}
		self.background_color = 'black'
		self.loop_count = 0
		self.querysetup = True
		self.save_button = LabelNode('Save Setup', font = ('Helvetica', 14), position = (700, 250), color = 'white')
		self.add_child(self.save_button)
		self.find_game_button = LabelNode('Find Game', position = (700,200), font=('Helvetica', 14), color = 'white')
		self.add_child(self.find_game_button)
		self.game_title = LabelNode('Tactics Mobile Arena', position = (550,400), color='white')
		self.add_child(self.game_title)
		self.looking_for_game = False
		for x in range(11):
			for y in range(11):
				if b[x][y][2]==1:
					self.tile_dict[(x,y)]=(b[x][y][0] * 41, b[x][y][1]*27+5)
					self.tile = SpriteNode('tile.png', position=(b[x][y][0] * 41, b[x][y][1]*27+5), scale=.7)
					self.add_child(self.tile)
				elif b[x][y][2]==2:
					
					self.tile_dict[(x,y)]=(b[x][y][0] * 41, b[x][y][1]*27+5)
					self.tile = SpriteNode('tile2.png', position=(b[x][y][0] * 41, b[x][y][1]*27+5), scale=.7)
					self.add_child(self.tile)
		self.active_piece = None
		self.z =[
		[9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
		[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
		[7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
		[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
		[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
		[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
		[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
		[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
		[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
		[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
		[0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
		self.e = [
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 'mg', 0, 0, 'k', 0, 0, 0, 0, 0, 0],
		['c', 0, 0, 0, 0, 0, 'k', 'k', 0, 0, 0],
		[0, 0, 'd', 'k', 0, 'k', 'k', 'k', 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 'k', 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 'k', 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
		self.sprite_info_dict={
		'k':['knight',1,.7],
		's':['scout',1, .7],
		'c':['cleric',1, .7],
		'fg':['fgolem',1, .6],
		'mg':['mgolem',1, .6],
		'sg':['sgolem',1, .7],
		'f':['furgon',1, .7],
		'd':['dragon',2, .5],
		'br':['brider',1, .5]
		}
		self.get_setup()
		self.update_pieces()
	def update(self):
		self.loop_count+=1
		if self.loop_count%60==0 and self.looking_for_game:
			r=requests.get(server_ip+'check_game_ready', cookies=client.login_request.cookies)
			print(str(r.content))
			if r.content==b'ready':
				self.looking_for_game= False
				client.switch_to_game()
	def get_setup(self):
		r = requests.get(server_ip+'get_setup',cookies=client.login_request.cookies)
		self.e = eval(r.content)
	def update_pieces(self):
		self.unit_dict={}
		for x in range(11):
			for y in range(11):
				if self.e[x][y] is not 0:
					sprite_name = "sprites/%s/%s_1_s.png"%(self.sprite_info_dict[self.e[x][y]][0],self.sprite_info_dict[self.e[x][y]][0])
					
					self.unit_dict[(x,y)]=SpriteNode(sprite_name, position=(b[x][y][0]*41+3, b[x][y][1]*27-5), scale = self.sprite_info_dict[self.e[x][y]][2])
					self.unit_dict[(x,y)].anchor_point = (0.5,0)
					self.unit_dict[(x,y)].z_position = self.z[x][y]
					self.add_child(self.unit_dict[(x,y)])

	def check_valid_placement(self, ix, iy):
		if self.e[ix][iy] is not 0:
			return False
			
		ox, oy = self.original_e_index
		self.e[ix][iy]=self.e[ox][oy]
		self.e[ox][oy]=0
		pop_count = 0
		for i in range(11):
			for j in range(5):
				if self.e[i][j] is not 0:
					pop_count+=self.sprite_info_dict[self.e[i][j]][1]
		if pop_count>10:
			self.e[ox][oy]=self.e[ix][iy]
			self.e[ix][iy]=0
			return False			
		
		return True
	def get_tile_index(self, x,y):	
		for ind, pos in self.tile_dict.items():
			pt1 = [pos[0], pos[1]+self.tile.size[1]/2] 
			pt2 = [pos[0]+self.tile.size[0]/2, pos[1]]
			pt3 = [pos[0], pos[1]-self.tile.size[1]/2]
			pt4 = [pos[0]-self.tile.size[0]/2, pos[1]]
			tile_path = mpath.Path(np.array([[pt1[0],pt1[1]],
													 [pt2[0],pt2[1]],
													 [pt3[0],pt3[1]],
													 [pt4[0],pt4[1]]]))
			if tile_path.contains_point((x,y)): 
				px, py = ind
				return pos, px, py
		return None
	def touch_began(self, touch):
		x, y = touch.location
		sx, sy, sw, sh = self.save_button.bbox
		if sx<x<sx+sw and sy<y<sy+sh:
			r = requests.post(server_ip+'update_setup', data={'setup': str(self.e)}, cookies =client.login_request.cookies)
			print("setup saved")
		fx, fy, fw, fh = self.find_game_button.bbox
		if fx<x<fx+fw and fy<y<fy+fh:
			print("finding game")
			r = requests.get(server_ip+'find_game', cookies=client.login_request.cookies)
			
			self.looking_for_game = True
		for unit_pos, sprite in self.unit_dict.items():
			xmin = sprite.position.x-sprite.size[0]/2
			xmax = sprite.position.x+sprite.size[0]/2
			ymin = sprite.position.y
			ymax = sprite.position.y +sprite.size[1]
			if  xmin <x< xmax and ymin<y<ymax:
				self.original_e_index = self.get_tile_index(sprite.position.x,sprite.position.y)[1:3]
				self.active_piece = sprite
				self.piece_original = self.active_piece.position
	def touch_moved(self,touch):
		if self.active_piece:
			self.active_piece.position = (touch.location.x,touch.location.y)
	def touch_ended(self, touch):
		if self.active_piece:
			x,y = touch.location
			p = self.get_tile_index(x,y)
			if p:
				pos, ix, iy = p
				if self.check_valid_placement(ix,iy):
					self.active_piece.position = (pos[0]+4,pos[1]-10)
					self.active_piece.z_position=self.z[ix][iy]
					self.piece_original = self.active_piece.position
				else:
					self.active_piece.position = self.piece_original
			else:
				self.active_piece.position = self.piece_original		
			self.active_piece = None

class SwitchViews(ui.View):
	def __init__(self):
		self.login_view = self.create_login_view()
		self.login_view.flex = 'WH'
		
		self.scene_view = SceneView()
		self.scene_view.frame = (0,0,736, 414)
		self.scene_view.scene = login()
		
		self.game_view = SceneView()
		self.game_view.frame = (0,0,736,414)
		self.game_view.scene = game_scene()
		
		#self.add_subview(self.scene_view)
		self.add_subview(self.login_view)
		
		self.background_color = 'white'
		self.present(style = 'sheet', hide_title_bar=True)
		self.login_request = None
	def switch_to_game(self):
		self.scene_view.hidden = True
		self.add_subview(self.game_view)
	def login_to_setup(self):
		self.login_view.hidden=True
		self.add_subview(self.scene_view)
	def create_login_view(self):
		def login_tapped(sender):
			self.login_request = requests.post(server_ip+'login', data = {'username':view['username'].text, 'password':view['password'].text})
			if 'authenticated' in str(self.login_request.content):
				self.login_to_setup()
		def register_tapped(sender):
			r = requests.post(server_ip+'register', data = {'username':view['username'].text, 'password':view['password'].text})
		#view=ui.View()	
		view = ui.View(frame=(0,0,736, 414))
		view.background_color = 'white'
		username = ui.TextField(frame=(view.width/2-70,view.height/2-80,140,25))
		username.name = 'username'
		username.alignment = ui.ALIGN_CENTER
		username.placeholder = 'username'
		view.add_subview(username)
		
		password = ui.TextField(frame=(view.width/2-70, view.height/2-50, 140, 25))
		password.name = 'password'
		password.secure = True
		password.alignment = ui.ALIGN_CENTER
		password.placeholder = 'password'
		view.add_subview(password)
		
		login_button = ui.Button(name = 'login', frame=(view.width/2-70, view.height/2-20, 65, 25))
		login_button.title = 'Login'
		login_button.border_color = 'blue'
		login_button.border_width = 1 
		login_button.corner_radius = 5
		login_button.action = login_tapped
		view.add_subview(login_button)
		
		register_button = ui.Button(name = 'Register', frame = (view.width/2, view.height/2-20, 65, 25))
		register_button.title = 'Register'
		register_button.border_color = 'blue'
		register_button.border_width = 1
		register_button.corner_radius = 5
		register_button.action = register_tapped
		view.add_subview(register_button) 
		return view
client = SwitchViews()
