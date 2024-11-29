#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-29 21:33
FileName: P0589. N 叉树的前序遍历
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

        def dfs(root):
            if not root:
                return
            values.append(root.val)
            for child in root.children:
                dfs(child)

        return values


if __name__ == '__main__':
    solution = Solution().preorder(Node(0))
