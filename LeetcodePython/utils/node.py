#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 17:14
FileName: node
Description:
"""
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        if not self:
            return ''
        values, cur = [], self
        while cur:
            values.append(str(cur.val))
            cur = cur.next
        return '[' + ','.join(values) + ']'

    @classmethod
    def create(cls, data=''):
        if not data:
            return []
        values = data[1:-1].split(',')
        dummy = ListNode(-1)
        cur = dummy
        for v in values:
            cur.next = ListNode(int(v))
            cur = cur.next
        return dummy.next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        if not self:
            return ''
        queue = deque([self])
        values = []
        while queue:
            node = queue.popleft()
            if node:
                values.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                values.append('null')
        while values[-1] == 'null':
            values.pop()
        return '[' + ','.join(values) + ']'

    @classmethod
    def create(cls, data=''):
        if not data:
            return []
        values = data[1:-1].replace(' ', '').split(',')
        root = TreeNode(int(values[0].strip()))
        queue = deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if i < len(values) and values[i] != 'null':
                node.left = TreeNode(int(values[i].strip()))
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] != 'null':
                node.right = TreeNode(int(values[i].strip()))
                queue.append(node.right)
            i += 1
        return root


if __name__ == '__main__':
    ll = ListNode.create('[1,2,3,4,5]')
    print(ll)

    tree = TreeNode.create("[4,8,5,0,1,null,6]")
    print(tree)
