#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-15 22:37
FileName: P1672. 最富有客户的资产总量
Description:
"""
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(row) for row in accounts])


if __name__ == '__main__':
    solution = Solution().maximumWealth(accounts=[[1, 5], [7, 3], [3, 5]])
    print(solution)
