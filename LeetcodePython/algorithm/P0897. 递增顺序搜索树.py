#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-29 22:10
FileName: P0897. 递增顺序搜索树
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nodes.append(root)
            dfs(root.right)

        dfs(root)

        for i, node in enumerate(nodes[:-1]):
            node.left = None
            node.right = nodes[i + 1]
        nodes[-1].left = None
        nodes[-1].right = None
        return nodes[0]


if __name__ == '__main__':
    root = TreeNode().create('[5,3,6,2,4,null,8,1,null,null,null,7,9]')
    solution = Solution().increasingBST(root)
    print(solution)
