#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-05 18:03
FileName: P2816. 翻倍以链表形式表示的数字
Description:
"""
from typing import Optional

from icecream import ic

from utils.node import ListNode


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        ans, carry = [], 0
        while values or carry:
            if values:
                carry += values.pop() * 2
            carry, mod = divmod(carry, 10)
            ans.append(mod)

        dummy = curr = ListNode(-1)
        while ans:
            curr.next = ListNode(ans.pop())
            curr = curr.next
        return dummy.next


if __name__ == '__main__':
    head = ListNode.create('[0]')
    solution = Solution().doubleIt(head)
    ic(solution.__str__())
