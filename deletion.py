from binary_tree import Node

# function to delete the given deepest node (d_node) in binary tree  
def deleteDeepest(root,d_node): 
    q = [] 
    q.append(root) 
    while(len(q)): 
        temp = q.pop(0) 
        if temp is d_node: 
            temp = None
            return
        if temp.right: 
            if temp.right is d_node: 
                temp.right = None
                return
            else: 
                q.append(temp.right) 
        if temp.left: 
            if temp.left is d_node: 
                temp.left = None
                return
            else: 
                q.append(temp.left) 
   
# function to delete element in binary tree  
def deletion(root, key): 
    if root == None : 
        return None
    if root.left == None and root.right == None: 
        if root.key == key :  
            return None
        else : 
            return root 
    key_node = None
    q = [] 
    q.append(root) 
    while(len(q)): 
        temp = q.pop(0) 
        if temp.data == key: 
            key_node = temp 
        if temp.left: 
            q.append(temp.left) 
        if temp.right: 
            q.append(temp.right) 
    if key_node :  
        x = temp.data 
        deleteDeepest(root,temp) 
        key_node.data = x 
    return root 








# Use the insert method to add nodes

root = Node(25)
root.insert(12)
root.insert(10)
root.insert(22)
root.insert(5)
root.insert(36)
root.insert(30)
root.insert(40)
root.insert(28)
root.insert(38)
root.insert(48)

deletion(root,38)

"""
# 25,36,20,10,5,22,40,48,38,30,22,12,28
root = Node(25)
root.insert(36)
root.insert(20)
root.insert(10)
root.insert(5)
root.insert(22)
root.insert(40)
root.insert(48)
root.insert(38)
root.insert(30)
root.insert(12)
root.insert(28)

print(root.sizeTree(),root.depth())

"""
