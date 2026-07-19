#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 23:39
FileName: P0590. N 叉树的后序遍历.py
Description:
"""
from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        values = []

        def dfs(node: 'Node'):
            if not node:
                return
            for child in node.children:
                dfs(child)
            values.append(node.val)

        dfs(root)
        return values


if __name__ == '__main__':
    solution = Solution()
    print(solution)
