#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-07 08:55
FileName: 面试题/LCR 024. 反转链表.py
Description: 
"""

from utils.node import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recurse(pre, cur):
            if not cur:
                return pre
            ans = recurse(cur, cur.next)
            cur.next = pre
            return ans

        return recurse(None, head)


if __name__ == '__main__':
    solution = Solution().reverseList(ListNode([1, 2, 3, 4, 5]))
    print(solution)
