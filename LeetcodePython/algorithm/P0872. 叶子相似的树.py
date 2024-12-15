#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-15 19:57
FileName: P0872. 叶子相似的树
Description:
"""
from typing import Optional

from utils.node import TreeNode


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leafs(node, leafs):
            if not node:
                return
            get_leafs(node.left, leafs)
            get_leafs(node.right, leafs)
            if node.left is None and node.right is None:
                leafs.append(node.val)

        leafs1, leafs2 = [], []
        get_leafs(root1, leafs1)
        get_leafs(root2, leafs2)
        return leafs1 == leafs2


if __name__ == '__main__':
    root1 = TreeNode.create('[3,5,1,6,2,9,8,null,null,7,4]')
    root2 = TreeNode.create('[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]')
    solution = Solution().leafSimilar(root1, root2)
    print(solution)
