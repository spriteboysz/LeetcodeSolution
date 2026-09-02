#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-02 09:37
FileName: 面试题/面试题 04.03. 特定深度节点链表.py
Description: 
"""
from collections import deque
from typing import Optional, List

from utils.node import TreeNode, ListNode


class Solution:
    def listOfDepth(self, tree: Optional[TreeNode]) -> List[Optional[ListNode]]:
        levels = []
        if not tree:
            return levels

        queue = deque([tree])
        while queue:
            dummy = ListNode(-1)
            curr = dummy
            for i in range(len(queue)):
                node = queue.popleft()
                curr.next = ListNode(node.val)
                curr = curr.next
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            levels.append(dummy.next)
        return levels


if __name__ == '__main__':
    solution = Solution().listOfDepth(TreeNode('[1,2,3,4,5,null,7,8]'))
    print(solution)
