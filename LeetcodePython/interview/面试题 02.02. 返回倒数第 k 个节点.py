#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-22 19:47
FileName: 面试题 02.02. 返回倒数第 k 个节点
Description:
"""
from typing import Optional

from utils.node import ListNode


class Solution:
    def kthToLast(self, head: Optional[ListNode], k: int) -> int:
        num, curr = 0, head
        while curr:
            num += 1
            curr = curr.next
        curr = head
        num -= k
        while curr:
            if num == 0:
                return curr.val
            curr = curr.next
            num -= 1
        return -1


if __name__ == '__main__':
    head = ListNode.create('[1,2,3,4,5]')
    solution = Solution().kthToLast(head, 2)
    print(solution)
