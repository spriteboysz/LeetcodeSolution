#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-04-05 15:52:05
LastEditTime: 2022-04-05 15:56:31
Description: 
FilePath: 328.奇偶链表.py
"""
#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        even = evencur = head
        odd = oddcur = head.next
        while evencur.next and oddcur.next:
            evencur.next = evencur.next.next
            oddcur.next = oddcur.next.next
            evencur, oddcur = evencur.next, oddcur.next
        evencur.next = odd
        return head


# @lc code=end
