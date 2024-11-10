#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 17:14
FileName: node
Description:
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self:
            return ""
        values, cur = [], self
        while cur:
            values.append(str(cur.val))
            cur = cur.next
        return "[" + ",".join(values) + "]"

    @classmethod
    def create(cls, data=""):
        if not data:
            return []
        values = data[1:-1].split(',')
        dummy = ListNode(-1)
        cur = dummy
        for v in values:
            cur.next = ListNode(int(v))
            cur = cur.next
        return dummy.next


if __name__ == '__main__':
    ll = ListNode.create('[1,2,3,4,5]')
    print(ll)
