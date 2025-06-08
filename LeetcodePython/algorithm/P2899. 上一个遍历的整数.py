#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-06-07 17:32
FileName: algorithm/P2899. 上一个遍历的整数.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen, ans, k = [], [], 0
        for num in nums:
            if num != -1:
                seen.insert(0, num)
                k = 0
            else:
                k += 1
                if k <= len(seen):
                    ans.append(seen[k - 1])
                else:
                    ans.append(-1)
        return ans


if __name__ == '__main__':
    solution = Solution().lastVisitedIntegers(nums=[1, 2, -1, -1, -1])
    ic(solution)
