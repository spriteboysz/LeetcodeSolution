#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-15 21:44
FileName: P0701. 二叉搜索树中的插入操作.py
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        def build(nums: list) -> Optional[TreeNode]:
            if not nums:
                return None
            mid = len(nums) // 2
            return TreeNode(
                nums[mid],
                left=build(nums[:mid]),
                right=build(nums[mid + 1:])
            )

        values = []
        dfs(root)
        values.append(val)
        values.sort()
        return build(values)


if __name__ == '__main__':
    solution = Solution().insertIntoBST(TreeNode('[4,2,7,1,3]'), 5)
    print(solution)
