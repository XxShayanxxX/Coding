from binarytree import Node

#create root node 
root = Node(1)

#create.left = Node(2)
root.left = Node(2)
root.right = Node(3)

#Add more nodes to the left subtree 
root.left.left = Node(4)
root.left.right = Node(5)

#Add more nodes to the right subtree 
root.right.left = Node(6)
root.right.right = Node(7)

#Display the binary tree 
print("Binary Tree Structure: ")
print(root)

#In-order traversal to display the tree nodes 
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.value, end=" ")
        in_order_traversal(node.right)

#Pre-order traversal to display the tree nodes 
def pre_order_traversal(node):
    if node:
        print(node.value,end = ' ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

#Post-order traversal to display the tree 
def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value, end=" ")

#Display the tree nodes using different transversals 

print("\nIn-order Transversal:")
in_order_traversal(root)
print("\n")

print("Pre-order Transversal:")
pre_order_traversal(root)
print("\n")

print("Post-order Transversal:")
post_order_traversal(root)
print("\n")
