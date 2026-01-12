for x in range(get_world_size()) :
	for y in range(get_world_size()) :	
		move(North)
		if get_ground_type() != Grounds.Soil :
			till()
	move(East)