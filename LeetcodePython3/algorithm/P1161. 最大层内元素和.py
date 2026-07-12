#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-12 21:54
FileName: P1161. 最大层内元素和.py
Description:
"""
from collections import deque
from typing import Optional

from utils.node import TreeNode


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels = []
        if not root:
            return -1
        queue = deque([root])
        while queue:
            level = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level += int(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
        maximum = max(levels)
        for i, v in enumerate(levels):
            if v == maximum:
                return i + 1
        return -1


if __name__ == '__main__':
    solution = Solution().maxLevelSum(TreeNode('[1,7,0,7,-8,null,null]'))
    print(solution)
