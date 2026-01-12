def carrot() :
	if get_ground_type() != Grounds.Soil :
		till()
	plant(Entities.Carrot)

def sunflower_harvest() :
	if get_ground_type() != Grounds.Soil :
		till()
	plant(Entities.Sunflower)
	if can_harvest() and measure() >= 7 :
		harvest()
		plant(Entities.Sunflower)
	