import defplant
import defdowater

while True :
	for x in range(get_world_size()) :
		for y in range(get_world_size()):
			if get_pos_x() == 0 :
				defplant.sunflower_harvest()
				defowater.usewater(0.05)
			elif get_ground_type() != Grounds.Grassland :
				till()
			if can_harvest() :
				harvest()
			move(North)
		
		move(East)	