#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-18 23:13
FileName: P0728. 自除数
Description:
"""
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = []
        for num in range(left, right + 1):
            if all([i != 0 and num % i == 0 for i in map(int, list(str(num)))]):
                nums.append(num)
        return nums


if __name__ == '__main__':
    solution = Solution().selfDividingNumbers(1, 22)
    print(solution)
