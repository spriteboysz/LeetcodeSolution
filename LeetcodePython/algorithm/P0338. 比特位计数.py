#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 23:41
FileName: P0338. 比特位计数
Description:
"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        return [i.bit_count() for i in range(n + 1)]

if __name__ == '__main__':
    solution = Solution().countBits(5)
    print(solution)