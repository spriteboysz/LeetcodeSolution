#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-04 22:31
FileName: P0102. 二叉树的层序遍历
Description:
"""
from typing import Optional, List
from collections import deque

from utils.node import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
            levels.append(level.copy())
        return levels


if __name__ == '__main__':
    root = TreeNode.create('[3,9,20,null,null,15,7]')
    solution = Solution().levelOrder(root)
    print(solution)
