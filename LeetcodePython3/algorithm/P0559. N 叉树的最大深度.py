#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 23:31
FileName: P0559. N 叉树的最大深度.py
Description:
"""
from collections import deque
from typing import Optional, List


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        levels = 0
        if not root:
            return levels

        queue = deque([root])
        while queue:
            levels += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for child in node.children:
                    if not child:
                        continue
                    queue.append(child)
        return levels


if __name__ == '__main__':
    solution = Solution().maxDepth(Node(-1))
    print(solution)
