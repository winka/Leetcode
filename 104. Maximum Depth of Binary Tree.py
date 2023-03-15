

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

TN = TreeNode(val=[3,9,20,1,9,15,7])
print(TN.left)

deque([TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None},
       right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None},
       right: TreeNode{val: 7, left: None, right: None}}}])


TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None},
right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None},
right: TreeNode{val: 7, left: None, right: None}}}