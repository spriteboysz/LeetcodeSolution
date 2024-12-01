#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-01 20:32
FileName: P0942. 增减字符串匹配
Description:
"""
from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        nums = list(range(len(s) + 1))
        ret = []
        for ch in s:
            if ch == 'I':
                ret.append(nums[0])
                nums = nums[1:]
            else:
                ret.append(nums.pop())
        return ret + nums


if __name__ == '__main__':
    solution = Solution().diStringMatch("IDID")
    print(solution)
