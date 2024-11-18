#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-18 22:45
FileName: P2544. 交替数字和
Description:
"""

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        return sum(map(int, str(n)[::2])) - sum(map(int, str(n)[1::2]))

if __name__ == '__main__':
    solution = Solution().alternateDigitSum(521)
    print(solution)