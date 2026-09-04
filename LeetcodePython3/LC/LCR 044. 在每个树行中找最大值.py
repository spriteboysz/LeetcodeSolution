#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 21:38
FileName: LC/LCR 044. 在每个树行中找最大值.py
Description: 
"""
from collections import deque
from typing import List

from utils.node import TreeNode


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        levels, level = [], []
        if not root:
            return levels

        queue = deque([root])
        while queue:
            level.clear()
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(max(level))
        return levels


if __name__ == '__main__':
    solution = Solution().largestValues(TreeNode('[1,3,2,5,3,null,9]'))
    print(solution)
