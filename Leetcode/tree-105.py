# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder or not preorder:
            return None

        val = preorder.pop(0)
        node = TreeNode(val)
        idx = inorder.index(val)

        node.left = self.buildTree(preorder, inorder[:idx])
        node.right = self.buildTree(preorder, inorder[idx+1:])

        return root
    """

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_map = {value: index for index, value in enumerate(inorder)}
        pre_iter = iter(preorder)


        def _helper(start, end):
            if start > end:
                return None
            root_val = next(pre_iter)
            root = TreeNode(root_val)
            idx = inorder_map[root_val]

            root.left = _helper(start, idx-1)
            root.right = _helper(idx+1, end)
            return root
        return _helper(0, len(inorder) - 1)