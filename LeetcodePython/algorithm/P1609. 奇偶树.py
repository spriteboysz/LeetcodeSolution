#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-08 12:45
FileName: P1609. 奇偶树
Description:
"""
from collections import deque
from typing import Optional

from utils.node import TreeNode


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        high, queue = 0, deque()
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
            if high % 2 == 0:
                for num in level:
                    if num % 2 != 1:
                        return False
                for i in range(1, len(level)):
                    if level[i - 1] >= level[i]:
                        return False
            else:
                for num in level:
                    if num % 2 != 0:
                        return False
                for i in range(1, len(level)):
                    if level[i - 1] <= level[i]:
                        return False
            high += 1
        return True


if __name__ == '__main__':
    root = TreeNode.create('[1,10,4,3,null,7,9,12,8,6,null,null,2]')
    solution = Solution().isEvenOddTree(root)
    print(solution)
