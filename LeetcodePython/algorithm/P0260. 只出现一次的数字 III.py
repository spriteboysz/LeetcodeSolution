#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-06 21:23
FileName: P0260. 只出现一次的数字 III
Description:
"""
from collections import defaultdict
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1
        return [num for num, cnt in dic.items() if cnt == 1]


if __name__ == '__main__':
    solution = Solution().singleNumber(nums=[1, 2, 1, 3, 2, 5])
    print(solution)
