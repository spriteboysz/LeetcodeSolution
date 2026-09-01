#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-01 21:44
FileName: LCR/LCR 045. 找树左下角的值.py
Description: 
"""
from collections import deque

from utils.node import TreeNode


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        left = 0
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if i == 0:
                    left = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return left


if __name__ == '__main__':
    solution = Solution().findBottomLeftValue(TreeNode('[2,1,3]'))
    print(solution)
