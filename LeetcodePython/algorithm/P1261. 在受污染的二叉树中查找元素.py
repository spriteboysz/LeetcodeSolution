#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-15 9:25
FileName: algorithm/P1261. 在受污染的二叉树中查找元素.py
Description: 
"""
from typing import Optional

from icecream import ic

from utils.node import TreeNode


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()

        def dfs(node, val):
            if not node:
                return
            self.values.add(val)
            dfs(node.left, val * 2 + 1)
            dfs(node.right, val * 2 + 2)

        dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.values


if __name__ == '__main__':
    solution = FindElements(TreeNode.create('[-1,-1,-1,-1,-1]'))
    ic(solution.find(1))
    ic(solution.find(3))
    ic(solution.find(5))
