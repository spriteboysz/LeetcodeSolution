#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-08 11:44
FileName: P0700. 二叉搜索树中的搜索
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)


if __name__ == '__main__':
    root = TreeNode().create('[4,2,7,1,3]')
    solution = Solution().searchBST(root, 5)
    print(solution)
