#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-12 21:20
FileName: P0513. 找树左下角的值.py
Description:
"""
from collections import deque
from typing import Optional

from utils.node import TreeNode


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        value = -1
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if i == 0:
                    value = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return value


if __name__ == '__main__':
    solution = Solution().findBottomLeftValue(TreeNode('[1,2,3,4,null,5,6,null,null,7]'))
    print(solution)
