#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-05 23:25
FileName: node
Description:
"""

from collections import deque
from typing import Union, Any


class ListNode:
    """
    链表类
    """

    def __init__(self, val: Any = 0, next_=None):
        if isinstance(val, str) and val.strip().startswith('[') and val.strip().endswith(']'):
            val = val.strip()[1:-1].split(',')
        if isinstance(val, list):
            head = self._build(val)
            if isinstance(head, ListNode):
                self.val = head.val
                self.next = head.next
        else:
            self.val = val
            self.next = next_

    def __str__(self):
        if not self:
            return ''
        values, curr = [], self
        while curr:
            values.append(str(curr.val))
            curr = curr.next
        return '<ListNode>: [' + ', '.join(values) + ']'

    @classmethod
    def _build(cls, values: Union[list]):
        if not values:
            return None

        curr = dummy = ListNode(-1)
        for value in values:
            if isinstance(value, int):
                value = int(value)
            curr.next = ListNode(value)
            curr = curr.next
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
    ll = ListNode([1, 2, 3, 4, 5])
    print(ll)

    tree = TreeNode.create("[4,8,5,0,1,null,6]")
    print(tree)
