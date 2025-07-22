"""
In a binary tree,  each node has at most two children, with the left child containing values less than the parent node
and the right child containing values greater than the parent node, allowing for efficient searching and sorting operations.

"""

class TreeNode:
    # self parameter represents the instance of the class being created
    # key represented the value to be stored in the node
    def __init__(self, key):
        # the key attribute of the TreeNode instance will be set to the value passed during the object's creation
        self.key = key

        #initializing the left and right children of the node, a node does not has any children when it is first created
        self.left = None
        self.right = None

#BinarySearchTree class represents a binary search tree
class BinarySearchTree:
    def __init__(self):
        #root represents the root node of the Binary Tree
        #when binary tree is first created the root node is empty thats why it is set to None
        self.root = None

    #The _insert method is a helper function, it will be used by insert() function later on.
    #It is recursive function, it will call itself to transverse the tree until the appropriate location for new node is found
    def _insert(self, node, key):
        if node is None: #that is if there is no value in that node
            #The below line creates a new Treenode instance with the provided key
            return TreeNode(key)
        
        #if the value of key is less, it is places in the left daughter node
        if key<node.key:
            #_insert method is recursively called to add the key to the left daughter node
            node.left = self._insert(node.left, key)

        # if the value of key is greater, it is placed in the right daughter node
        elif key > node.key:
            node.right = self._insert(node.right, key)

        #returning the node structure to update the tree structure
        return node
    
    #This function will be called by the user
    def insert(self, key):
        pass
    