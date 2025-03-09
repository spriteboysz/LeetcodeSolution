#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-09 21:40
FileName: LCR/LCR 055. 二叉搜索树迭代器.py
Description: 
"""

from icecream import ic

from utils.node import TreeNode


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.values = []
        self.dfs(root)
        self.values.reverse()

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.values.append(root.val)
        self.dfs(root.right)

    def next(self) -> int:
        if self.hasNext():
            return self.values.pop()
        return -1

    def hasNext(self) -> bool:
        return bool(self.values)


if __name__ == '__main__':
    root1 = TreeNode.create('[7, 3, 15, null, null, 9, 20]')
    solution = BSTIterator(root1)
    ic(solution.next())
    ic(solution.next())
    ic(solution.next())
    ic(solution.hasNext())
