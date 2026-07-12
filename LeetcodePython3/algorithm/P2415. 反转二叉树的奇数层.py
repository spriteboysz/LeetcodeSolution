#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-12 09:44
FileName: P2415. 反转二叉树的奇数层.py
Description:
"""
from collections import deque
from typing import Optional

from utils.node import TreeNode


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        level = 0
        queue = deque([root])
        while queue:
            values, nodes = [], []
            for _ in range(len(queue)):
                node = queue.popleft()
                nodes.append(node)
                values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            for node, v in zip(nodes, values[::-1]):
                if level % 2 == 1:
                    node.val = v
            level += 1
        return root

if __name__ == '__main__':
    solution = Solution().reverseOddLevels(TreeNode([2, 3, 5, 8, 13, 21, 34]))
    print(solution)
