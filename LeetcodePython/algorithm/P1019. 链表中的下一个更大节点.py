#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 20:09
FileName: P1019. 链表中的下一个更大节点
Description:
"""
from typing import Optional, List

from icecream import ic

from utils.node import ListNode


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        stack = []
        n = len(values)
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= values[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(values[i])
        return ans


if __name__ == '__main__':
    head = ListNode.create('[2,7,4,3,5]')
    solution = Solution().nextLargerNodes(head)
    ic(solution)
