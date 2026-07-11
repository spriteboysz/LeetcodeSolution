#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 11:23
FileName: P0237. 删除链表中的节点.py
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


if __name__ == '__main__':
    solution = Solution()
    print(solution)
