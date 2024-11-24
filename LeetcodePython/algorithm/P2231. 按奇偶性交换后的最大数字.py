#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-23 23:01
FileName: P2231. 按奇偶性交换后的最大数字
Description:
"""


class Solution:
    def largestInteger(self, num: int) -> int:
        nums = [int(digit) for digit in str(num)]
        nums1 = [num for num in nums if num % 2 == 1]
        nums1.sort()
        nums0 = [num for num in nums if num % 2 == 0]
        nums0.sort()
        for i, num in enumerate(nums):
            if num % 2 == 0:
                nums[i] = nums0.pop()
            else:
                nums[i] = nums1.pop()
        return int(''.join(map(str, nums)))


if __name__ == '__main__':
    solution = Solution().largestInteger(247)
    print(solution)
