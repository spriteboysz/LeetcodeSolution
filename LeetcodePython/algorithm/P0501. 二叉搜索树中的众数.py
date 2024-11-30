#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-29 23:26
FileName: P0501. 二叉搜索树中的众数
Description:
"""
from typing import Optional, List

from utils.node import TreeNode
from collections import defaultdict


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = defaultdict(int)

        def dfs(node):
            if not node:
                return
            dic[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        maximum = max(dic.values())
        return [val for val, cnt in dic.items() if cnt == maximum]


if __name__ == '__main__':
    root = TreeNode().create('[1,null,2,2]')
    solution = Solution().findMode(root)
    print(solution)
