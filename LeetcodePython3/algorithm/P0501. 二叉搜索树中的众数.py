#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-13 22:42
FileName: P0501. 二叉搜索树中的众数.py
Description:
"""
from typing import Optional, List, Counter

from utils.node import TreeNode


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        values = []
        dfs(root)
        counter = Counter(values)
        maximum = max(counter.values())
        return [num for num, cnt in counter.items() if cnt == maximum]


if __name__ == '__main__':
    solution = Solution().findMode(TreeNode('[1,null,2,2,1,3]'))
    print(solution)
