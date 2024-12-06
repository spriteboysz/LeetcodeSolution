#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-05 22:44
FileName: P0109. 有序链表转换二叉搜索树
Description:
"""
from typing import Optional

from utils.node import ListNode, TreeNode


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        values = []
        while head:
            values.append(head.val)
            head = head.next

        def create(left, right):
            if left >= right:
                return None
            mid = left + (right - left) // 2
            node = TreeNode(values[mid])
            node.left = create(left, mid)
            node.right = create(mid + 1, right)
            return node

        return create(0, len(values))


if __name__ == '__main__':
    head = ListNode().create('[-10,-3,0,5,9]')
    solution = Solution().sortedListToBST(head)
    print(solution)
