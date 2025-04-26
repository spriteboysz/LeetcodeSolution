#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-26 14:27
FileName: interview/面试题 17.17. 多次搜索.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        results = []
        for small in smalls:
            if not small:
                results.append([])
                continue
            result = [i for i in range(len(big)) if small == big[i:i + len(small)]]
            results.append(result)
        return results


if __name__ == '__main__':
    solution = Solution().multiSearch(
        big="mississippi",
        smalls=["is", "ppi", "hi", "sis", "i", "ssippi"])
    ic(solution)
