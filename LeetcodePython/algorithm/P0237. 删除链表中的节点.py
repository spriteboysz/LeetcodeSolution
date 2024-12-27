#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-27 22:05
FileName: P0237. 删除链表中的节点
Description:
"""


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
