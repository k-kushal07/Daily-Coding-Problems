class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def count_unival_subtrees(root, count):
    if root == None:
        return True
        
    left = count_unival_subtrees(root.left, count)
    right = count_unival_subtrees(root.right, count)
        
    if left == False or right == False:
        return False
        
    if root.left and root.left.data != root.data:
        return False
        
    if root.right and root.right.data != root.data:
        return False
        
    count[0] += 1
    return True
    
def count_unival(root):
    count = [0]
        
    count_unival_subtrees(root, count)
        
    return count[0]

root = Node('a') 
root.left = Node('b') 
root.right = Node('a') 
root.left.left = Node('b') 
root.left.right = Node('b') 
root.right.right = Node('a') 

print(f"There are {countSingle(root)} unival sub-trees ") 
