#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-10 22:57
FileName: P2415. 反转二叉树的奇数层
Description:
"""
from collections import deque
from typing import Optional

from icecream import ic

from utils.node import TreeNode


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        queue = deque([root])
        level = 0
        while queue:
            values, nodes = [], []
            for i in range(len(queue)):
                node = queue.popleft()
                values.append(node.val)
                nodes.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2 == 1:
                for node, val in zip(nodes, values[::-1]):
                    node.val = val
            level += 1
        return root


if __name__ == '__main__':
    root = TreeNode.create('[2,3,5,8,13,21,34]')
    solution = Solution().reverseOddLevels(root)
    ic(solution.__str__())
