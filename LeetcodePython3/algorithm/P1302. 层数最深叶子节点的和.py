#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-11 21:47
FileName: P1302. 层数最深叶子节点的和.py
Description:
"""
from collections import deque
from typing import Optional

from utils.node import TreeNode


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue, ans = deque([root]), 0
        while queue:
            ans = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                ans += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans


if __name__ == '__main__':
    solution = Solution().deepestLeavesSum(TreeNode('[1,2,3,4,5,null,6,7,null,null,null,null,8]'))
    print(solution)
