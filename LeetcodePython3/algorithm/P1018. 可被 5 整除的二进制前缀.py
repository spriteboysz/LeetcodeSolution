#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-14 11:29
FileName: P1018. 可被 5 整除的二进制前缀.py
Description:
"""
from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans, curr = [], 0
        for num in nums:
            curr = curr * 2 + num
            ans.append(curr % 5 == 0)
        return ans


if __name__ == '__main__':
    solution = Solution().prefixesDivBy5([0, 1, 1])
    print(solution)
