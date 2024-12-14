#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-14 14:13
FileName: LCR 027. 回文链表
Description:
"""
from utils.node import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values == values[::-1]


if __name__ == '__main__':
    head = ListNode.create('[1,2,3,3,2,1]')
    solution = Solution().isPalindrome(head)
    print(solution)
