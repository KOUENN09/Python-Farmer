import defgoto

measure_flower = {7:[], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[]}
for x in range(get_world_size()) :
	for y in range(get_world_size()) :
		if get_ground_type() != Grounds.Soil :
			till()
		plant(Entities.Sunflower)
		measure_flower[measure()].append([get_pos_x(), get_pos_y()]) 
		move(North)
	move(East)

for i in range(15, 6, -1) :
	for j in measure_flower[i] :
		defgoto.tothere(j[0], j[1])
		harvest()