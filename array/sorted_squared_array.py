def sortedSquaredArr(array):
	sqrArr = []
	
	for num in range(len(array)):
		squardNum = array[num]**2
		sqrArr.append(squardNum)

	sqrArr.sort()
    return sqrArr
