#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-16 15:30
FileName: 面试题/面试题 02.03. 删除中间节点.py
Description: 
"""
from utils.node import ListNode


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    solution = Solution().deleteNode(ListNode(5))
    print('<None>' if solution is None else f'{solution=}')
