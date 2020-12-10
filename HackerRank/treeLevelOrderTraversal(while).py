

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""




def levelOrder(root):
    nodeQueue = [root]
    levelList = []
    while nodeQueue:
        if nodeQueue[0].left:
            nodeQueue.append(nodeQueue[0].left)
        if nodeQueue[0].right:
            nodeQueue.append(nodeQueue[0].right)
    
        levelList.append(nodeQueue[0].info)
        nodeQueue.pop(0)
    else:
        print(' '.join(map(str, levelList)))
    
    
    
