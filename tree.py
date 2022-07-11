class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def inOrder(root:TreeNode, lst:list):
    if not root:
        return None
    inOrder(root.left, lst)
    lst.append(root.val)
    inOrder(root.right, lst)

def preOrder(root, lst):
    if not root:
        return None
    lst.append(root.val)
    preOrder(root.left, lst)
    preOrder(root.right, lst)

def postOrder(root, lst):
    if not root:
        return None
    postOrder(root.left, lst)
    postOrder(root.right, lst)
    lst.append(root.val)

if __name__ == '__main__':
    lf1 = TreeNode(3)
    lf2 = TreeNode(4)
    lf11 = TreeNode(2,lf1,lf2)
    rf1 = TreeNode(6)
    rf2 = TreeNode(7)
    rf11 = TreeNode(5, rf1, rf2)
    root = TreeNode(1, lf11, rf11)
    lst_mid = []
    inOrder(root, lst_mid)
    print(lst_mid)
    lst_pre = []
    preOrder(root, lst_pre)
    print(lst_pre)
    lst_post = []
    postOrder(root, lst_post)
    print(lst_post)
