#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-29 22:02
FileName: P0590. N 叉树的后序遍历
Description:
"""
from typing import Optional, List


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        values = []

        def dfs(root):
            if not root:
                return
            for child in root.children:
                dfs(child)
            values.append(root.val)

        dfs(root)
        return values
