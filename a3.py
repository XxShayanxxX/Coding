from binarytree import build 

class Node:
    # A class representing a node in a binary tree 

    def __init__(self,key):
        self.right = None
        self.left = None 
        self.val = key


def print_preorder(root):
    #Recursively performs a pre-order traversal of the binary tree 

    if root :
        #Print the data of the node
        print(root.val, end = " ")

        #Recursively traverse the left subtree 
        print_preorder(root.left)

        #Recursively traverse the right subtree 
        print_preorder(root.right)


if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

# Using the binarytree module to visualise the tree structure 
# Convert the tree into a binarytree node structure 
    tree_list = [1,2,3,4,5]
    visual_tree = build(tree_list)

    #Printing pre-order traversal 
    print("preorder traversal of vbinary tree is: ")
    print_preorder(root)
    print()