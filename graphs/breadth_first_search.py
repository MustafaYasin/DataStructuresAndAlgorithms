class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
		queue = [self]
		
		while queue:
			current = queue.pop(0)
			
			queue.extend(current.children)
			array.append(current.name)
		
		return array
		
		