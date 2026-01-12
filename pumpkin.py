import defbreakloop
import defgoto
#numharvest记录收获次数。
#numharvest = 0
while defbreakloop.shouldbreakon(1) :
	#start = get_time()
	#numRipe每次遍历前归零，全部can_harvest则harvest
	numRipe = 0
	while numRipe != (get_world_size() * get_world_size()) :
		numRipe = 0
		for x in range(get_world_size()) :	
			for y in range(get_world_size()) :
				if get_ground_type() != Grounds.Soil :
					till()
				plant(Entities.Pumpkin)
				move(North)
				if can_harvest() :
					numRipe += 1
			move(East)
	#print(n)
	#if numRipe == (get_world_size() * get_world_size()) :
	defgoto.tothere()
	#print(get_time() - start)
	harvest()