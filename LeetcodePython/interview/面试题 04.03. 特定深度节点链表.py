#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-22 21:03
FileName: 面试题 04.03. 特定深度节点链表
Description:
"""
from collections import deque
from typing import Optional, List

from utils.node import TreeNode, ListNode


class Solution:
    def listOfDepth(self, tree: Optional[TreeNode]) -> List[Optional[ListNode]]:
        if not tree:
            return []
        levels, queue = [], deque([tree])
        while queue:
            dummy = head = ListNode(-1)
            for _ in range(len(queue)):
                node = queue.popleft()
                head.next = ListNode(node.val)
                head = head.next
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(dummy.next)
        return levels


if __name__ == '__main__':
    root = TreeNode.create('[1,2,3,4,5,null,7,8]')
    solution = Solution().listOfDepth(root)
    for head in solution:
        print(head)
