# create binary tree and perform inorder,preorder,postorder recursive traversal
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def create():
    x = int(input("enter data to create node(0 to stop): "))
    if x==0:
        return None
    root= node(x)
    print(f"Enter left of {x}:")
    root.left=create()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    print(f"Enter right of {x}:")
    root.right =create()
    return root

def preorder(root):
    if root is not None:
        print(root.data)
        # root= root.left
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data)


root=create()
print("Preorder")
preorder(root)
print("Inorder")
inorder(root)
print("Postorder")
postorder(root)
