#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 21:32
FileName: P1672. 最富有客户的资产总量.py
Description:
"""
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(account) for account in accounts)


if __name__ == '__main__':
    solution = Solution().maximumWealth(accounts=[[1, 2, 3], [3, 2, 1]])
    print(solution)
