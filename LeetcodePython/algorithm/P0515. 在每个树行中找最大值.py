#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-06 22:59
FileName: P0515. 在每个树行中找最大值
Description:
"""
from collections import deque
from typing import List, Optional

from utils.node import TreeNode


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        levels, queue = [], deque()
        queue.append(root)
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(max(level))
        return levels


if __name__ == '__main__':
    root = TreeNode.create('[1,3,2,5,3,null,9]')
    solution = Solution().largestValues(root)
    print(solution)
