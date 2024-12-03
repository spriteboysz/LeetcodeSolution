#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-02 23:09
FileName: P0559. N 叉树的最大深度
Description:
"""
from typing import Optional, List


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        return max([self.maxDepth(child) for child in root.children]) + 1
