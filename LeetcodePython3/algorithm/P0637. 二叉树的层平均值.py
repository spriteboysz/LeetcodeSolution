#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-12 21:38
FileName: P0637. 二叉树的层平均值.py
Description:
"""
from collections import deque
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        average = []
        if not root:
            return average

        queue = deque([root])
        while queue:
            values = []
            for _ in range(len(queue)):
                node = queue.popleft()
                values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            average.append(sum(values) / len(values))
        return average


if __name__ == '__main__':
    solution = Solution().averageOfLevels(TreeNode('[3,9,20,null,null,15,7]'))
    print(solution)
