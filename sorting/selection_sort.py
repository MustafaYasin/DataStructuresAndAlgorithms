def selectionSort(array):
	
    for i in range(len(array) - 1):
		for j in range(i+1, len(array)):
			if array[i] > array[j]:
				selectionswap(i, j, array)
	return array

def selectionswap(i,  j, array):
	array[i], array[j] = array[j], array[i]
	return array
