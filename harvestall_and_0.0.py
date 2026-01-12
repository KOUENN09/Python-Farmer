def harvest_all() :
	for n in range(get_world_size()) :
		move(East)
		harvest()
		for n in range(get_world_size()) :
			move(North)
			harvest()

for n in range(get_world_size()) :
	move(East)
	harvest()
	
	for n in range(get_world_size()) :
		move(North)
		harvest()

if get_pos_x() > 0 or get_pos_y() > 0 :
	while get_pos_x() > 0 : 
		move(West)
	while get_pos_y() > 0 : 
		move(South)