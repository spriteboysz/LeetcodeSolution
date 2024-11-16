#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-16 17:20
FileName: P1646. 获取生成数组中的最大值
Description:
"""


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0, 1]
        for i in range(2, n + 1):
            if i % 2 == 0:
                nums.append(nums[i // 2])
            else:
                nums.append(nums[i // 2] + nums[i // 2 + 1])
        return 0 if n == 0 else max(nums)


if __name__ == '__main__':
    solution = Solution().getMaximumGenerated(7)
    print(solution)
