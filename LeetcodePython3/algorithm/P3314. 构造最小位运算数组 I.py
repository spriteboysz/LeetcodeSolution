#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-09 09:46
FileName: P3314. 构造最小位运算数组 I.py
Description:
"""
from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            for i in range(1, num + 1):
                if i | (i + 1) == num:
                    ans.append(i)
                    break
            else:
                ans.append(-1)
        return ans


if __name__ == '__main__':
    solution = Solution().minBitwiseArray(nums=[11, 13, 31])
    print(solution)
