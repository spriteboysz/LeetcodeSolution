#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-11 23:33
FileName: P1305. 两棵二叉搜索树中的所有元素
Description:
"""
from typing import Optional, List

from icecream import ic

from utils.node import TreeNode


class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def dfs(root, values):
            if not root:
                return values
            dfs(root.left, values)
            values.append(root.val)
            dfs(root.right, values)
            return values

        values1 = dfs(root1, [])
        values2 = dfs(root2, [])
        return sorted(values1 + values2)


if __name__ == '__main__':
    root1 = TreeNode.create('[2,1,4]')
    root2 = TreeNode.create('[1,0,3]')
    solution = Solution().getAllElements(root1, root2)
    ic(solution)
