def pumpkin(plant_num = 1) :
	needmate_num = plant_num * get_cost(Entities.Pumpkin)[Items.Carrot]
	if num_items(Items.Carrot) >= needmate_num :
		return(True)
	else :
		return(False)