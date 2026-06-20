#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-20 11:14
FileName: P1646. 获取生成数组中的最大值.py
Description:
"""


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0, 1] + [0] * (n - 1)
        for i in range(2, n + 1):
            if i % 2 == 0:
                nums[i] = nums[i // 2]
            else:
                nums[i] = nums[i // 2] + nums[i // 2 + 1]
        return max(nums[:n + 1])


if __name__ == '__main__':
    solution = Solution().getMaximumGenerated(7)
    print(solution)
