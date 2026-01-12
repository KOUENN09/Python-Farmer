import defXandY
import defdowater
import defplant

while True :
	for x in range(get_world_size()) :
		for y in range(get_world_size()) :
			#print(get_pos_x() , get_pos_y())
			defdowater.usewater(0.08)
			if can_harvest() :
				harvest()
			#pos_x == 2 施肥
			if get_pos_x() == 2 :
				use_item(Items.Fertilizer)
				
			if defXandY.XY() % 2 == 0 :
				plant(Entities.Tree)
			#sunflower
			elif get_pos_x() <= 1 : 
				defplant.sunflower_harvest()
			#plant_another
			else :
				defplant.carrot()
				#plant(Entities.Bush)
				#defdowater.usewater()
			move(North)
		

		move(East)	