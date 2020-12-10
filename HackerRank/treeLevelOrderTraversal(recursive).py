

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

nodeQueue = []
levelList = []

def levelOrder(root):
    if root.left:
        nodeQueue.append(root.left)
    if root.right:
        nodeQueue.append(root.right)
    
    levelList.append(root.info)
    if nodeQueue:
        levelOrder(nodeQueue.pop(0))
    else:
        print(' '.join(map(str, levelList)))