#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-06 20:01
FileName: P0401. 二进制手表.py
Description:
"""
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for i in range(12 * 60):
            hh, mm = divmod(i, 60)
            if hh.bit_count() + mm.bit_count() == turnedOn:
                ans.append(f'{hh}:{mm:02d}')
        return ans


if __name__ == '__main__':
    solution = Solution().readBinaryWatch(1)
    print(solution)
