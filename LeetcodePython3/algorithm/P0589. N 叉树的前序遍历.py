#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 23:37
FileName: P0589. N 叉树的前序遍历.py
Description:
"""
from typing import Optional, List


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        values = []

        def dfs(node: 'Node'):
            if not node:
                return
            values.append(node.val)
            if not node.children:
                return
            for child in node.children:
                dfs(child)
        dfs(root)
        return values


if __name__ == '__main__':
    solution = Solution()
    print(solution)
