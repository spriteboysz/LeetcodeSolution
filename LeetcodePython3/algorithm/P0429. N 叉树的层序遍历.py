#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 10:54
FileName: P0429. N 叉树的层序遍历.py
Description:
"""
from collections import deque
from typing import Optional, List


class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        levels = []
        if not root:
            return levels
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if not node.children:
                    continue
                for child in node.children:
                    if not child:
                        continue
                    queue.append(child)
            levels.append(level)
        return levels


if __name__ == '__main__':
    solution = Solution().levelOrder(Node(1))
    print(solution)
