#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-01 19:42
FileName: P0401. 二进制手表
Description:
"""
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times = []
        for i in range(12 * 60):
            hh, mm = divmod(i, 60)
            if hh.bit_count() + mm.bit_count() == turnedOn:
                times.append(f'{hh}:{mm:02d}')
        return times


if __name__ == '__main__':
    solution = Solution().readBinaryWatch(1)
    print(solution)
