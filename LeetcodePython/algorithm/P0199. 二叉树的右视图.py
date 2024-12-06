#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-06 21:10
FileName: P0199. 二叉树的右视图
Description:
"""
from collections import deque
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        levels, queue = [], deque()
        queue.append(root)
        while queue:
            right = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                right = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(right)
        return levels


if __name__ == '__main__':
    root = TreeNode.create('[1,2,3,null,5,null,4]')
    solution = Solution().rightSideView(root)
    print(solution)
