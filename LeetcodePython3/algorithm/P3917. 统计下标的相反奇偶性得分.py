#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-01 09:08
FileName: algorithm/P3917. 统计下标的相反奇偶性得分.py
Description: 
"""


class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        counts = []
        for i, num1 in enumerate(nums):
            cnt = 0
            for num2 in nums[i + 1:]:
                if (num1 + num2) % 2 == 1:
                    cnt += 1
            counts.append(cnt)
        return counts


if __name__ == '__main__':
    solution = Solution().countOppositeParity([1, 2, 3, 4])
    print(solution)
