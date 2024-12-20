#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-20 21:10
FileName: LCP 44. 开幕式焰火
Description:
"""
from utils.node import TreeNode


class Solution:
    def numColor(self, root: TreeNode) -> int:
        seen = set()

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            seen.add(node.val)

        dfs(root)
        return len(seen)


if __name__ == '__main__':
    root = TreeNode.create('[1,3,2,1,null,2]')
    solution = Solution().numColor(root)
    print(solution)
