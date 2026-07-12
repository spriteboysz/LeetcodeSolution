#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-12 22:01
FileName: P0515. 在每个树行中找最大值.py
Description:
"""
from collections import deque
from typing import List, Optional

from utils.node import TreeNode


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        levels = []
        if not root:
            return levels
        queue = deque([root])
        while queue:
            values = []
            for _ in range(len(queue)):
                node = queue.popleft()
                values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(max(values))
        return levels


if __name__ == '__main__':
    solution = Solution().largestValues(TreeNode('[1,3,2,5,3,null,9]'))
    print(solution)
