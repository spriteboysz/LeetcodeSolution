#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-12 10:13
FileName: P0107. 二叉树的层序遍历 II.py
Description:
"""
from collections import deque
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        queue = deque([root])
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
    solution = Solution().levelOrderBottom(TreeNode('[3,9,20,null,null,15,7]'))
    print(solution)
