#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-22 19:38
FileName: 面试题 02.01. 移除重复节点
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def removeDuplicateNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        seen = {head.val}
        curr = head
        while curr.next:
            if curr.next.val not in seen:
                seen.add(curr.next.val)
                curr = curr.next
            else:
                curr.next = curr.next.next
        return head


if __name__ == '__main__':
    head = ListNode.create('[1, 2, 3, 3, 2, 1]')
    solution = Solution().removeDuplicateNodes(head)
    print(solution)
