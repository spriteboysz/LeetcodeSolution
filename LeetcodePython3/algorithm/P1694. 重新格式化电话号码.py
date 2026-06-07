#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-07 20:14
FileName: P1694. 重新格式化电话号码.py
Description:
"""


class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = [ch for ch in number if ch.isdigit()]
        segments = [digits[i:i + 3] for i in range(0, len(digits), 3)]
        if len(segments[-1]) == 1:
            segments[-1].insert(0, segments[-2].pop())
        return '-'.join(''.join(segment) for segment in segments)


if __name__ == '__main__':
    solution = Solution().reformatNumber(number="--17-5 229 35-39475 ")
    print(solution)
