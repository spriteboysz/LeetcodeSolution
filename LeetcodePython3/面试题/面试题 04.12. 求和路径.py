#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-08 08:58
FileName: 面试题/面试题 04.12. 求和路径.py
Description: 
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        def dfs(node, curr):
            if not node:
                return 0
            cnt = 0
            if node.val == curr:
                cnt += 1
            cnt += dfs(node.left, curr - node.val)
            cnt += dfs(node.right, curr - node.val)
            return cnt

        if not root:
            return 0
        return dfs(root, target) + self.pathSum(root.left, target) + self.pathSum(root.right, target)


if __name__ == '__main__':
    solution = Solution().pathSum(
        TreeNode('[5,4,8,11,null,13,4,7,2,null,null,5,1]'), 22
    )
    print('<None>' if not solution else f'{solution=}')
