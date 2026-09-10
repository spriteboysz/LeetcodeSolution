#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-05 18:31
FileName: 面试题/LCR 056. 两数之和 IV - 输入二叉搜索树.py
Description: 
"""
from utils.node import TreeNode


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def dfs(node: TreeNode) -> None:
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        values = []
        dfs(root)
        left, right = 0, len(values) - 1
        while left < right:
            if values[left] + values[right] == k:
                return True
            if values[left] + values[right] < k:
                left += 1
            else:
                right -= 1
        return False


if __name__ == '__main__':
    solution = Solution().findTarget(TreeNode('[8,6,10,5,7,9,11]'), 12)
    print(solution)
