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
        if node is None:
            return TreeNode(key)
        if key<node.key:
            pass

    