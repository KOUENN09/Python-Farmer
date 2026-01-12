import defgoto
import defbreakloop

while defbreakloop.shouldbreakon() :
	#n记录收割过几次仙人掌，判断是否结束
	numharvest = 0
	print("Harvested", numharvest, "times")
	numharvest += 1
	defgoto.tothere() #回到原点
	
	#遍历种植
	for x in range(get_world_size()) :
		for y in range(get_world_size()) :
			if get_ground_type() != Grounds.Soil :
				till()
			plant(Entities.Cactus)
			move(North)
		move(East)

	#排序，先沿y方向排序，再沿x方向排序，大的在上在右。
	#只要swap则NeedSwap = True。未swap则NeedSwap = False while结束 收割。 
	for x in range(get_world_size()) :
		NeedSwap = True
		while NeedSwap :
			NeedSwap = False
			for y in range(get_world_size()) :
				if get_pos_y() != get_world_size() - 1 :
					if measure() > measure(North) :
						swap(North)
						NeedSwap = True
				move(North)
	
		move(East)
	
	for y in range(get_world_size()) :
		NeedSwap = True
		while NeedSwap :
			NeedSwap = False
			for x in range(get_world_size()) :
				if get_pos_x() != get_world_size() - 1 :
					if measure() > measure(East) :
						swap(East)
						NeedSwap = True
				move(East)
		move(North)
		
	if not NeedSwap :
		harvest()