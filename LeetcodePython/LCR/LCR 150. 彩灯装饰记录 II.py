#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 19:19
FileName: LCR 150. 彩灯装饰记录 II
Description:
"""
from collections import deque
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels, queue = [], deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level)
        return levels


if __name__ == '__main__':
    root = TreeNode.create('[8,17,21,18,null,null,6]')
    solution = Solution().decorateRecord(root)
    print(solution)
