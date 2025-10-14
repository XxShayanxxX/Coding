from binarytree import build

class Node:
    #A Class representing a node in binary tree.

    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


def print_postorder(root):
    #Recursively performs a post-order traversal of the binary tree.

    if root:
        #Recursively traverse the left subtree 
        print_postorder(root.left)

        #Recursively traverse the right subtree 
        print_postorder(root.right)

if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

#Using the binary tree module to visualise the tree structure 
#COnvert the tree into a binarytree node structure 

    tree_list = [1,2,3,4,5]
    visual_tree = build(tree_list)

    print("binary tree visualization")
    print(visual_tree)

    #Printing post-order traversal 
    print("Post-order traversal of binary tree is: ")
    print_postorder(root)
    print()



        