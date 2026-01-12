import defbreakloop
import defgoto
import defmaterial
#numharvest记录收获次数。
#numharvest = 0
while defbreakloop.shouldbreakon(3) and defmaterial.pumpkin(2 * get_world_size() * get_world_size()):
	listx = []
	listy = []
	#start = get_time()
	defgoto.tothere()
	for n in range(2) : #第一次种植，第二次补种记录补种位置。
		for x in range(get_world_size()) :	
			for y in range(get_world_size()) :
				if get_ground_type() != Grounds.Soil :
					till()
				plant(Entities.Pumpkin)
				move(North)
				if n == 1 and not can_harvest() :
					listx.append(get_pos_x())
					listy.append(get_pos_y())
			move(East)

			
	while listx :
		#for n in range(len(listx) - 1， -1， -1) :
		n = 0 #while 方法
		while n < len(listx) :
			defgoto.tothere(listx[n], listy[n])
			#do_a_flip()
			if can_harvest() :
				listx.pop(n)
				listy.pop(n)
			else :
				plant(Entities.Pumpkin)
				n += 1

	defgoto.tothere()
	#print(get_time() - start)
	harvest()
	