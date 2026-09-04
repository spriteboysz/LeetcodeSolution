#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 09:48
FileName: LC/LCR 151. 彩灯装饰记录 III.py
Description: 
"""

from collections import deque
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[List[int]]:
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
            if len(levels) % 2 == 0:
                levels.append(level.copy())
            else:
                levels.append(level[::-1])
        return levels


if __name__ == '__main__':
    solution = Solution().decorateRecord(TreeNode('[8,17,21,18,null,null,6]'))
    print(solution)
