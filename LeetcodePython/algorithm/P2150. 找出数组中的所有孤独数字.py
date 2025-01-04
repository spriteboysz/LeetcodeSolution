#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-04 21:20
FileName: P2150. 找出数组中的所有孤独数字
Description:
"""
from collections import Counter
from typing import List

from icecream import ic


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return [num for num, cnt in counter.items() if cnt == 1 and num - 1 not in counter and num + 1 not in counter]


if __name__ == '__main__':
    solution = Solution().findLonely(nums=[10, 6, 5, 8])
    ic(solution)
