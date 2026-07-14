#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-13 22:26
FileName: P1609. 奇偶树.py
Description:
"""
from collections import deque
from itertools import pairwise
from sys import path
from typing import Optional

from utils.node import TreeNode


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        level, queue = 0, deque([root])
        while queue:
            values = []
            for _ in range(len(queue)):
                node = queue.popleft()
                values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2 == 0:
                if any(v % 2 == 0 for v in values) or any(v1 >= v2 for v1, v2 in pairwise(values)):
                    return False
            else:
                if any(v % 2 == 1 for v in values) or any(v1 <= v2 for v1, v2 in pairwise(values)):
                    return False
            level += 1
        return True


if __name__ == '__main__':
    solution = Solution().isEvenOddTree(TreeNode('[1,10,4,3,null,7,9,12,8,6,null,null,2]'))
    print(solution)
