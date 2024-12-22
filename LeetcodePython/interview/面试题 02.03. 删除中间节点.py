#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-22 20:39
FileName: 面试题 02.03. 删除中间节点
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
    head = ListNode.create('[4,1,5,9]')
    node = ListNode(5)
    Solution().deleteNode(node)
