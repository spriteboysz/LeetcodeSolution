#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-05 22:39
FileName: P0107. 二叉树的层序遍历 II
Description:
"""
from collections import deque
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
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
            levels.append(level)
        return levels[::-1]


if __name__ == '__main__':
    root = TreeNode().create('[3,9,20,null,null,15,7]')
    solution = Solution().levelOrderBottom(root)
    print(solution)
