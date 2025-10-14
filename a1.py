from binarytree import build

class Node:
    #A class representing a node in a binary tree 
    def __init__(self,key):
        self.right = None
        self.left = None
        self.val = key 


def print_inorder(root):
    #Recursively performs an in-order traversal of the binary tree.
    if root :
        #recursively traverse the left subtree 
        print_inorder(root.left)

        #Print the data of the node 
        print(root.val,end = " ")

        #recursively transverse the right subtree
        print_inorder(root.right)

if __name__  == "__main__":
    #Constructing the binary tree 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    #Using the binarytree module to visualise the tree structure 
    # COnvert the tree into a binarytree structure node 

    treelist = [ 1,2,3,4,5]
    visual_tree = build(treelist)

    print("binary tree visualization")
    print(visual_tree)

    #printing pre-order traversal 
    print("Preorder traversal of binary tree is: ")
    print_inorder(root)
    print()