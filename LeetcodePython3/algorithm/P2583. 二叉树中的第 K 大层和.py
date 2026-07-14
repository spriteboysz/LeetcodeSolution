#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-13 23:00
FileName: P2583. 二叉树中的第 K 大层和.py
Description:
"""
from collections import deque
from typing import Optional

from utils.node import TreeNode


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        levels = []
        queue = deque([root])
        while queue:
            level = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
        levels.sort(reverse=True)
        try:
            return levels[k - 1]
        except IndexError:
            return -1


if __name__ == '__main__':
    solution = Solution().kthLargestLevelSum(TreeNode('[5,8,9,2,1,3,7,4,6]'), 2)
    print(solution)
