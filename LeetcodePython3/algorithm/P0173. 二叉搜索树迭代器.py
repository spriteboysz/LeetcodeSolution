#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-08 16:23
FileName: algorithm/P0173. 二叉搜索树迭代器.py
Description: 
"""
from collections import deque
from typing import Optional

from utils.node import TreeNode


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.queue = deque()

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.queue.append(node.val)
            dfs(node.right)

        dfs(root)

    def next(self) -> int:
        return self.queue.popleft()

    def hasNext(self) -> bool:
        return bool(self.queue)


if __name__ == '__main__':
    solution = BSTIterator(TreeNode('[7, 3, 15, null, null, 9, 20]'))
    print(solution.next())
    print(solution.hasNext())
