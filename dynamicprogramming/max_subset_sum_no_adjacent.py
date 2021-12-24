def maxSubsetSumNoAdjacent(array):
	if len(array) == 0:
		return 0
	if len(array) == 1:
		return array[0]
	else:
		firstSum = array[0]
		secondSum = max(array[0], array[1])
		for i in range(2, len(array)):
			result = max(secondSum, firstSum + array[i])
			firstSum, secondSum = secondSum, result
		return secondSum
