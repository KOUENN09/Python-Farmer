while True:
	if can_harvest() :
		harvest()
		if get_ground_type() != Grounds.Soil :
			till() 
		plant(Entities.Carrot)
		#plant(Entities.Bush)
		move(North)
	else: 
		move(East)