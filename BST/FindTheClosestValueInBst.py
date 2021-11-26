def findClosestValueInBst(tree, target, minValue=None):
    # Write your code here.
	if tree is None:
		return minValue
	if minValue is None:
		minValue = tree.value
	elif abs(tree.value - target) < abs(minValue - target):
		minValue = tree.value
	if tree.value < target:
		return findClosestValueInBst(tree.right, target, minValue)
	elif tree.value > target:
		return findClosestValueInBst(tree.left, target, minValue)
	else:
		return tree.value
		
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
