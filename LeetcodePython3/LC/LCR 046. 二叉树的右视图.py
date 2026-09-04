#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 21:41
FileName: LC/LCR 046. 二叉树的右视图.py
Description: 
"""
from collections import deque
from typing import List

from utils.node import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        levels, level = [], []
        if not root:
            return levels

        queue = deque([root])
        while queue:
            level.clear()
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(level[-1])
        return levels


if __name__ == '__main__':
    solution = Solution().rightSideView(TreeNode('[1,2,3,null,5,null,4]'))
    print(solution)
