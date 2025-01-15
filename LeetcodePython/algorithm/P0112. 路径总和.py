#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-14 23:13
FileName: P0112. 路径总和
Description:
"""
from typing import Optional

from icecream import ic

from utils.node import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        paths = set()

        def dfs(node, path):
            if not node:
                return
            path += node.val
            if not node.left and not node.right:
                paths.add(path)
            else:
                dfs(node.left, path)
                dfs(node.right, path)

        dfs(root, 0)
        return targetSum in paths


if __name__ == '__main__':
    root = TreeNode.create('[5,4,8,11,null,13,4,7,2,null,null,null,1]')
    solution = Solution().hasPathSum(root, 22)
    ic(solution)
