def usewater(limit = 1) :
	if get_water() <= limit :
		use_item(Items.Water)
		