class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
	currentNode = linkedList
	while currentNode:
		temp = currentNode.next
		while temp is not None and temp.value == currentNode.value:
			temp = temp.next
		
		currentNode.next = temp
		currentNode = temp
		
		
	return linkedList
