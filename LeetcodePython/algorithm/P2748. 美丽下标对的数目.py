#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-27 21:34
FileName: P2748. 美丽下标对的数目
Description:
"""
from typing import List
import math


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        cnt = 0
        for i, num2 in enumerate(nums):
            for num1 in nums[:i]:
                if math.gcd(int(str(num1)[0]), num2 % 10) == 1:
                    cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countBeautifulPairs(nums=[31, 25, 72, 79, 74])
    print(solution)
