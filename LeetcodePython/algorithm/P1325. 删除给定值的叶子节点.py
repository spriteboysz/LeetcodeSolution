#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-26 22:36
FileName: P1325. 删除给定值的叶子节点
Description:
"""
from typing import Optional

from icecream import ic

from utils.node import TreeNode


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if root.left is None and root.right is None and root.val == target:
            return None
        return root


if __name__ == '__main__':
    root = TreeNode.create('[1,2,3,2,null,2,4]')
    solution = Solution().removeLeafNodes(root, 2)
    ic(solution.__str__())
