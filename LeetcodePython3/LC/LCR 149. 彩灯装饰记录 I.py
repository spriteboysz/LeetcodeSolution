#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-04 09:26
FileName: LC/LCR 149. 彩灯装饰记录 I.py
Description: 
"""
from collections import deque
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[int]:
        levels = []
        if not root:
            return levels
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                levels.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return levels


if __name__ == '__main__':
    solution = Solution().decorateRecord(TreeNode('[8,17,21,18,null,null,6]'))
    print(solution)
