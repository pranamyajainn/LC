class Solution:
    def __init__(self):
        self.max_diameter = 0
    
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        self.getLength(root)
        return self.max_diameter
    
    def getLength(self, node):
        if not node:
            return 0
        left = self.getLength(node.left)
        right = self.getLength(node.right)
        self.max_diameter = max(self.max_diameter, left + right)
        return 1 + max(left, right)