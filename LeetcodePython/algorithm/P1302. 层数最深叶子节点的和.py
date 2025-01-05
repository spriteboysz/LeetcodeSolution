#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 20:52
FileName: P1302. 层数最深叶子节点的和
Description:
"""
from collections import deque
from typing import Optional

from icecream import ic

from utils.node import TreeNode


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        levels, queue = -1, deque([root])
        while queue:
            level = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels = level
        return levels


if __name__ == '__main__':
    root = TreeNode.create('[1,2,3,4,5,null,6,7,null,null,null,null,8]')
    solution = Solution().deepestLeavesSum(root)
    ic(solution)
