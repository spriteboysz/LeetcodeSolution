#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-19 23:20
FileName: P0721. 账户合并.py
Description:
"""
from typing import List
from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        pass


if __name__ == '__main__':
    solution = Solution().accountsMerge(
        accounts=[["John", "johnsmith@mail.com", "john00@mail.com"],
                  ["John", "johnnybravo@mail.com"],
                  ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                  ["Mary", "mary@mail.com"]]
    )
    print(solution)
