#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-04-19 21:38
FileName: LCP 51. 烹饪料理.py
Description:
"""
from typing import List


class Solution:
    def perfectMenu(self, materials: List[int], cookbooks: List[List[int]], attribute: List[List[int]],
                    limit: int) -> int:

        ans = 0  # 美味度
        n = len(cookbooks)

        def dfs(i, contribute):
            a, b = contribute  # 传美味度和饱腹感的一个元组
            if b >= limit:
                nonlocal ans
                ans = max(ans, a)
            if i == n:
                return

            for j in range(i, n):
                if all(x >= y for x, y in zip(materials, cookbooks[j])):
                    for k in range(len(materials)):  # 材料使用
                        materials[k] -= cookbooks[j][k]
                    dfs(j + 1, (a + attribute[j][0], b + attribute[j][1]))
                    for k in range(len(materials)):  # 材料还原
                        materials[k] += cookbooks[j][k]

        dfs(0, (0, 0))
        return ans if ans != 0 else -1


if __name__ == '__main__':
    solution = Solution().perfectMenu(
        materials=[3, 2, 4, 1, 2],
        cookbooks=[[1, 1, 0, 1, 2], [2, 1, 4, 0, 0], [3, 2, 4, 1, 0]],
        attribute=[[3, 2], [2, 4], [7, 6]],
        limit=5
    )
    print(solution)
