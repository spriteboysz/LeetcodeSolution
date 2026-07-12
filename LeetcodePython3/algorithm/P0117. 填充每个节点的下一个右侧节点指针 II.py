#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-12 21:36
FileName: P0117. 填充每个节点的下一个右侧节点指针 II.py
Description:
"""
from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = deque([root])
        while queue:
            nodes = []
            for _ in range(len(queue)):
                node = queue.popleft()
                nodes.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[i + 1]
        return root


if __name__ == '__main__':
    solution = Solution()
    print(solution)
