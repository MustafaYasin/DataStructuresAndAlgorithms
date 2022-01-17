##############################################################
# This is an iterative solution to the binary search problem #
##############################################################

def binarySearch(array, target):

	leftPointer = 0
	rightPointer = len(array) - 1
	
	while leftPointer <= rightPointer:
		midPointer = (rightPointer + leftPointer) // 2
		
		if target == array[midPointer]:
			return midPointer
		
		elif target > array [midPointer]:
			leftPointer = midPointer + 1
		
		else:
			rightPointer = midPointer - 1		
		
	return - 1


##############################################################
# This is a recursive solution to the binary search problem  #
##############################################################



def binarySearch(array, target):
    return helperBinarySearch(array, target, 0,len(array)-1)


def helperBinarySearch(array, target, leftPointer, rightPointer):
	
	while leftPointer <= rightPointer:
		midPointer = (leftPointer + rightPointer) // 2
		
		if target == array[midPointer]:
			return midPointer
		elif target > array[midPointer]:
			return helperBinarySearch(array, target, midPointer + 1, rightPointer)
		else:
			return helperBinarySearch(array, target, leftPointer, midPointer - 1)
		
	return - 1

	
	