import defbreakloop

while defbreakloop.shouldbreakon(1) :
	
	
	plant(Entities.Bush)
	substance = 10 * 2**(num_unlocked(Unlocks.Mazes) - 1)
	if num_items(Items.Weird_Substance) < substance :
		print("Not enough Weird_Substance")
		break
	use_item(Items.Weird_Substance, substance)
		
	direction = [North, East, South, West]
	index = 0
	#
	
		#右转 直行 左转 
	while get_entity_type() == Entities.Hedge :
		if can_move(direction[(index + 1) % 4]) :
			index =  (index + 1) % 4
			move(direction[index])
		elif can_move(direction[index]) :
			move(direction[index])
		else:
			index = (index - 1) % 4
			move(direction[index])
		
	if get_entity_type() == Entities.Treasure and defbreakloop.numloop < 2:
		#harvest()
		use_item(Items.Weird_Substance, substance)
	else :
		harvest()