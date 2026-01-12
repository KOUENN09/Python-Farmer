direction = [North, East, South, West]
index = 0
maze_size = 5 #迷宫大小
crossroad = False #记录是否是岔路口

plant(Entities.Bush)
substance = maze_size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)

if can_move(direction[index]) :
	move(direction[index])
elif can_move(direction[(index + 1) % 4]) :
	move(direction[(index + 1) % 4])
