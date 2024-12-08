#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-08 12:39
FileName: P1161. 最大层内元素和
Description:
"""
from collections import deque
from typing import Optional

from utils.node import TreeNode


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels, queue = [], deque()
        queue.append(root)
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
        maximum = max(levels)
        return [i + 1 for i, num in enumerate(levels) if num == maximum][0]


if __name__ == '__main__':
    root = TreeNode().create('[1,7,0,7,-8,null,null]')
    solution = Solution().maxLevelSum(root)
    print(solution)
