#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-17 22:04
FileName: P2160. 拆分数位后四位数字的最小和
Description:
"""


class Solution:
    def minimumSum(self, num: int) -> int:
        nums = list(map(int, sorted(list(str(num)))))
        return sum(nums[:2]) * 10 + sum(nums[2:])


if __name__ == '__main__':
    solution = Solution().minimumSum(4009)
    print(solution)
