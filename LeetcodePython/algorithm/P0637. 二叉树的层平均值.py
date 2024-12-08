#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-08 11:18
FileName: P0637. 二叉树的层平均值
Description:
"""
from collections import deque
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
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
            levels.append(sum(level) / len(level))
        return levels


if __name__ == '__main__':
    root = TreeNode().create('[3,9,20,null,null,15,7]')
    solution = Solution().averageOfLevels(root)
    print(solution)
