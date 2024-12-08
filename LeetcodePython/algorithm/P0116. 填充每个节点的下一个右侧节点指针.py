#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-08 21:52
FileName: P0116. 填充每个节点的下一个右侧节点指针
Description:
"""
from collections import deque
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        queue = deque()
        queue.append(root)
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
