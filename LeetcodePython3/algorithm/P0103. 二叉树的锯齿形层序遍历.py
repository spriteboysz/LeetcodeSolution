#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-13 22:14
FileName: P0103. 二叉树的锯齿形层序遍历.py
Description:
"""
from collections import deque
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
        for i, level in enumerate(levels):
            if i % 2 == 1:
                level[::] = level[::-1]
        return levels


if __name__ == '__main__':
    solution = Solution().zigzagLevelOrder(TreeNode('[3,9,20,null,null,15,7]'))
    print(solution)
