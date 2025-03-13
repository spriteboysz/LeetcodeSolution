#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-13 23:14
FileName: algorithm/P0173. 二叉搜索树迭代器.py
Description: 
"""
from typing import Optional

from icecream import ic

from utils.node import TreeNode


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.values = []

        def dfs(root1):
            if not root1:
                return
            dfs(root1.left)
            self.values.append(root1.val)
            dfs(root1.right)

        dfs(root)
        self.values.reverse()

    def next(self) -> int:
        if self.hasNext():
            return self.values.pop()
        return -1

    def hasNext(self) -> bool:
        return bool(self.values)


if __name__ == '__main__':
    tree = TreeNode.create('[7, 3, 15, null, null, 9, 20]')
    solution = BSTIterator(tree)
    ic(solution.next())
    ic(solution.next())
    ic(solution.hasNext())
