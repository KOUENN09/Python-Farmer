import defXandY
import defdowater
import defplant

while True :
	for x in range(get_world_size()) :
		for y in range(get_world_size()) :
			#print(get_pos_x() , get_pos_y())
			defdowater.useowater(0.05)
			if can_harvest() :
				harvest()
			if defXandY.XY() % 2 == 0 :
				plant(Entities.Tree)
				#defdowater.usewater()
			elif get_pos_x() <= 0 :
				defplant.sunflower_harvest()
			else :
				defplant.carrot()
			move(North)

		move(East)