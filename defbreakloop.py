numloop = 0 
def shouldbreakon(limitloop = None) :
#声明全局变量，第二次调用函数时numloop不会归零，
#但目前没有出现，若shouldbreakon()为空，则一直循环
#若numloop没有自动归零，在return后numloop = 0
	global numloop
	#print("harvested", numloop, "times")
	numloop += 1
	if limitloop == None :
		return(True)
	if numloop > limitloop :
		return (False)
	else : 
		return (True)