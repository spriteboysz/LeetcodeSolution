#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-02 23:24
FileName: LCR 056. 两数之和 IV - 输入二叉搜索树
Description:
"""
from utils.node import TreeNode


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        values = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        dfs(root)
        left, right = 0, len(values) - 1
        while left < right:
            total = values[left] + values[right]
            if total < k:
                left += 1
            elif total > k:
                right -= 1
            else:
                return True
        return False


if __name__ == '__main__':
    root = TreeNode.create('[8,6,10,5,7,9,11]')
    solution = Solution().findTarget(root, 12)
    print(solution)
