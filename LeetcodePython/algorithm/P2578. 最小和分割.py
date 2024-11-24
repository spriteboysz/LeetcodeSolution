#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 12:54
FileName: P2578. 最小和分割
Description:
"""


class Solution:
    def splitNum(self, num: int) -> int:
        nums = sorted(list(str(num)))
        return int(''.join(nums[::2])) + int(''.join(nums[1::2]))


if __name__ == '__main__':
    solution = Solution().splitNum(4325)
    print(solution)
