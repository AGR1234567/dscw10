class TreeNode:
    def __init__(self, data):
        self.data=data
        self.leftnode=None
        self.rightnode=None

root=TreeNode(1)
root.leftnode=TreeNode(2)
root.leftnode.leftnode=TreeNode(3)
root.leftnode.rightnode=TreeNode(4)
root.rightnode=TreeNode(5)
root.rightnode.leftnode=TreeNode(6)
root.rightnode.rightnode=TreeNode(7)

def inorder(root):
    if root.leftnode!=None:
        inorder(root.leftnode)
    