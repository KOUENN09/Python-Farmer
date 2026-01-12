# 缺少防绕圈功能。循环过程中迷宫移除某个墙体，不能及时优化路径

import defgoto
import defbreakloop

limit = 10    #循环次数
maze_size = 5 #迷宫大小

direction = [North, East, South, West]
listXY = [] #记录运动路径
listall = [] #若len(listall) == maze 面积则表示遍历完maze

plant(Entities.Bush)
substance = maze_size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)
	
		#右转 直行 左转 
index = 0 
while len(listall) < maze_size * maze_size :
	if can_move(direction[(index + 1) % 4]) :
		index =  (index + 1) % 4
		move(direction[index])
	elif can_move(direction[index]) : 
		move(direction[index])
	else:
		index = (index - 1) % 4
		move(direction[index])

	#listXY 记录运行路径 listall 判断是否遍历完整地图
	listXY.append((get_pos_x(), get_pos_y()))
	if (get_pos_x(), get_pos_y()) not in listall :
		listall.append((get_pos_x(), get_pos_y()))

	#遍历地图过程中路过Treasure，重置Treasure位置
	#if get_entity_type() == Entities.Treasure :
	#	use_item(Items.Weird_Substance, substance
lismeas = []
while defbreakloop.shouldbreakon(limit) :
	ltheway = [] #记录当前位置到Treasure的路径
	append_XY = False
	should_break_XY = 0

	#遍历listXY，当出现get_pox或measure()时，为True，代表可以ltheway.append
	for i in range(len(listXY) - 1, -1, -1) :

		#ltheway为空 并且listXY[i]为...。说明找到起点，append_XY为True，开始写入
		if (
			not ltheway and
			(listXY[i] == measure() or listXY[i] == (get_pos_x(), get_pos_y()))
		 ) :
			if listXY[i] == measure() :
				should_break_XY = (get_pos_x(), get_pos_y())
			else :
				should_break_XY = measure()				
			append_XY = True

		#删除分支，保证ltheway连续。原理：先删除两重复元素之间所有元素(包含重复元素)，
		#再写入listXY保证连续
		if append_XY :
			while listXY[i] in ltheway :
				ltheway.pop()
			ltheway.append(listXY[i])

		#ltheway不为空 并且listXY[i]为...。说明找到终点，添加最后一个坐标，break 。
		if ltheway and listXY[i] == should_break_XY :
			ltheway.append(listXY[i])
			break
	quick_print(ltheway)

	#调整ltheway正向遍历还是反向遍历，保证get_pos是起点，measure()是终点	
	if ltheway[0] == measure() :
		traversal_direction = range(len(ltheway)-1, -1,-1)
	else :
		traversal_direction = range(len(ltheway))
		
	for i in traversal_direction :
		x, y = ltheway[i]
		defgoto.tothere(x, y)
	do_a_flip()
	lismeas.append(measure())

	if get_entity_type() == Entities.Treasure and defbreakloop.numloop != limit :
		use_item(Items.Weird_Substance, substance)
	
if get_entity_type() == Entities.Treasure :
	harvest()