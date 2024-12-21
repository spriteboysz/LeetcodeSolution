#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-21 11:40
FileName: LCR 149. 彩灯装饰记录 I
Description:
"""
from collections import deque
from typing import Optional, List

from utils.node import TreeNode


class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        levels, queue = [], deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                levels.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return levels


if __name__ == '__main__':
    root = TreeNode.create('[8,17,21,18,null,null,6]')
    solution = Solution().decorateRecord(root)
    print(solution)
