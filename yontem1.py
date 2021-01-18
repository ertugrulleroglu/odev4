def minValueNode(node):
    current = node
 
    # loop down to find the leftmost leaf
    while(current.left is not None):
        current = current.left
 
    return current

 
 
def deleteNode(root, key):
 
    # Base Case
    if root is None:
        return root
 
    if key < root.data:
        root.left = deleteNode(root.left, key)
 
    elif(key > root.data):
        root.right = deleteNode(root.right, key)
 
   
    else:
 
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
 
        elif root.right is None:
            temp = root.left
            root = None
            return temp
 
        # Node with two children: 
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)
 
        # Copy the inorder successor's 
        # content to this node
        root.data = temp.data
 
        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.data)
 
    return root
