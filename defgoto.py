def tothere(x = 0, y = 0) :
	if x < get_pos_x() :
		while x < get_pos_x() : 
			move(West)
	else :
		while x > get_pos_x() : 
			move(East)
	
	if y < get_pos_y() : 
		while y < get_pos_y() : 
			move(South)
	else :
		while y > get_pos_y() : 
			move(North)
 