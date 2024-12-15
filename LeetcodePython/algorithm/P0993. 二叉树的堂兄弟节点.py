#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-15 20:23
FileName: P0993. 二叉树的堂兄弟节点
Description:
"""
from collections import deque
from typing import Optional

from utils.node import TreeNode


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        parent, queue = {}, deque([root])
        while queue:
            level = set()
            for _ in range(len(queue)):
                node = queue.popleft()
                level.add(node.val)
                if node.left:
                    queue.append(node.left)
                    parent.update({node.left.val: node.val})
                if node.right:
                    queue.append(node.right)
                    parent.update({node.right.val: node.val})
            if x in level and y in level:
                if parent.get(x, None) != parent.get(y, None):
                    return True
            elif x in level or y in level:
                return False
        return False


if __name__ == '__main__':
    root = TreeNode.create('[1,2,3,null,4,null,5]')
    solution = Solution().isCousins(root, 4, 5)
    print(solution)
