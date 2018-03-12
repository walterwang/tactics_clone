from scene import *
import ui
import matplotlib.path as mpath
import numpy as np

b=[[[0.0, 7.071, 0], [0.707, 6.364, 0], [1.414, 5.657, 1], [2.121, 4.95, 1], [2.828, 4.243, 1], [3.536, 3.536, 0], [4.243, 2.828, 2], [4.95, 2.121, 2], [5.657, 1.414, 2], [6.364, 0.707, 2], [7.071, 0.0, 2]], [[0.707, 7.778, 0], [1.414, 7.071, 1], [2.121, 6.364, 1], [2.828, 5.657, 1], [3.536, 4.95, 1], [4.243, 4.243, 0], [4.95, 3.536, 2], [5.657, 2.828, 2], [6.364, 2.121, 2], [7.071, 1.414, 2], [7.778, 0.707, 2]], [[1.414, 8.485, 1], [2.121, 7.778, 1], [2.828, 7.071, 1], [3.536, 6.364, 1], [4.243, 5.657, 1], [4.95, 4.95, 0], [5.657, 4.243, 2], [6.364, 3.536, 2], [7.071, 2.828, 2], [7.778, 2.121, 2], [8.485, 1.414, 2]], [[2.121, 9.192, 1], [2.828, 8.485, 1], [3.536, 7.778, 1], [4.243, 7.071, 1], [4.95, 6.364, 1], [5.657, 5.657, 0], [6.364, 4.95, 2], [7.071, 4.243, 2], [7.778, 3.536, 2], [8.485, 2.828, 2], [9.192, 2.121, 2]], [[2.828, 9.899, 1], [3.536, 9.192, 1], [4.243, 8.485, 1], [4.95, 7.778, 1], [5.657, 7.071, 1], [6.364, 6.364, 0], [7.071, 5.657, 2], [7.778, 4.95, 2], [8.485, 4.243, 2], [9.192, 3.536, 2], [9.899, 2.828, 2]], [[3.536, 10.607, 1], [4.243, 9.899, 1], [4.95, 9.192, 1], [5.657, 8.485, 1], [6.364, 7.778, 1], [7.071, 7.071, 0], [7.778, 6.364, 2], [8.485, 5.657, 2], [9.192, 4.95, 2], [9.899, 4.243, 2], [10.607, 3.536, 2]], [[4.243, 11.314, 1], [4.95, 10.607, 1], [5.657, 9.899, 1], [6.364, 9.192, 1], [7.071, 8.485, 1], [7.778, 7.778, 0], [8.485, 7.071, 2], [9.192, 6.364, 2], [9.899, 5.657, 2], [10.607, 4.95, 2], [11.314, 4.243, 2]], [[4.95, 12.021, 1], [5.657, 11.314, 1], [6.364, 10.607, 1], [7.071, 9.899, 1], [7.778, 9.192, 1], [8.485, 8.485, 0], [9.192, 7.778, 2], [9.899, 7.071, 2], [10.607, 6.364, 2], [11.314, 5.657, 2], [12.021, 4.95, 2]], [[5.657, 12.728, 1], [6.364, 12.021, 1], [7.071, 11.314, 1], [7.778, 10.607, 1], [8.485, 9.899, 1], [9.192, 9.192, 0], [9.899, 8.485, 2], [10.607, 7.778, 2], [11.314, 7.071, 2], [12.021, 6.364, 2], [12.728, 5.657, 2]], [[6.364, 13.435, 0], [7.071, 12.728, 1], [7.778, 12.021, 1], [8.485, 11.314, 1], [9.192, 10.607, 1], [9.899, 9.899, 0], [10.607, 9.192, 2], [11.314, 8.485, 2], [12.021, 7.778, 2], [12.728, 7.071, 2], [13.435, 6.364, 2]], [[7.071, 14.142, 0], [7.778, 13.435, 0], [8.485, 12.728, 1], [9.192, 12.021, 1], [9.899, 11.314, 1], [10.607, 10.607, 0], [11.314, 9.899, 2], [12.021, 9.192, 2], [12.728, 8.485, 2], [13.435, 7.778, 2], [14.142, 7.071, 2]]]
class login(Scene):
	def setup(self):
		self.tile_dict = {}
		self.background_color = 'black'
		self.querysetup=True
		
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
		self.sprite_info_dict={'k':['knight.png',1],
		's':['scout.png',1],
		'c':['cleric.png',1],
		'fg':['fgolem.png',1],
		'mg':['mgolem.png',1],
		'sg':['sgolem.png',1],
		'f':['furgon.png',1],
		'd':['dragon.png',2]
		}
	def get_setup(self):
		r = requests.get(server_ip+'get_setup',cookies=client.login_request.cookies)
		self.setup_array = r.content
	def update_pieces(self):
		self.unit_dict={}
		for x in range(11):
			for y in range(11):
				if self.e[x][y] is not 0:
					sprite_name = self.sprite_info_dict[self.e[x][y]][0]
					self.unit_dict[(x,y)]=SpriteNode(sprite_name, position=(b[x][y][0]*41+3, b[x][y][1]*27-5), scale = .7)
					self.unit_dict[(x,y)].anchor_point = (0.5,0)
					self.add_child(self.unit_dict[(x,y)])

	def update(self):
		try:
			if self.querysetup and client.login_request is not None:
				self.get_setup()
				self.update_pieces()
				self.querysetup = False
				print(self.setup_array)
		except:
			pass
			
			self.setup_pieces =False
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
		print(self.e)
		
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
		for unit_pos, sprite in self.unit_dict.items():
			xmin = sprite.position.x-sprite.size[0]/2
			xmax = sprite.position.x+sprite.size[0]/2
			ymin = sprite.position.y
			ymax = sprite.position.y +sprite.size[1]
			if  xmin <x< xmax and ymin<y<ymax:
				self.original_e_index = self.get_tile_index(sprite.position.x,sprite.position.y)[1:3]
				#self.active_pos_piece = unit_pos
				
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
					self.piece_original = self.active_piece.position
				else:
					self.active_piece.position = self.piece_original
			else:
				self.active_piece.position = self.piece_original		
			self.active_piece = None
			#self.update_pieces()
			
run(login(), LANDSCAPE)
