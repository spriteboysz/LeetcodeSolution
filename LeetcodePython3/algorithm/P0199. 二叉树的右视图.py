#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-12 21:31
FileName: P0199. 二叉树的右视图.py
Description:
"""
from collections import deque
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right = []
        if not root:
            return right

        queue = deque([root])
        while queue:
            val = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                val = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            right.append(val)
        return right


if __name__ == '__main__':
    solution = Solution().rightSideView(TreeNode('[1,2,3,4,null,null,null,5]'))
    print(solution)
