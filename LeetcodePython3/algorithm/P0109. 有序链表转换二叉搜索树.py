#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 11:37
FileName: P0109. 有序链表转换二叉搜索树.py
Description:
"""
from typing import Optional, List

from utils.node import ListNode, TreeNode


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def build(data: List[int]):
            if not data:
                return None
            mid = len(data) // 2
            node = TreeNode(data[mid])
            node.left = build(data[:mid])
            node.right = build(data[mid + 1:])
            return node

        values = []
        while head:
            values.append(head.val)
            head = head.next
        return build(values)


if __name__ == '__main__':
    solution = Solution().sortedListToBST(ListNode([-10, -3, 0, 5, 9]))
    print(solution)
