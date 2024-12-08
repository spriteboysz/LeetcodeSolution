#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-08 21:59
FileName: P0117. 填充每个节点的下一个右侧节点指针 II
Description:
"""
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = deque([root])
        while queue:
            for i in range(n := len(queue)):
                node = queue.popleft()
                if i == n - 1:
                    node.next = None
                else:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root
