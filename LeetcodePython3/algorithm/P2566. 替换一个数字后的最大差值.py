#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-28 11:39
FileName: P2566. 替换一个数字后的最大差值.py
Description:
"""


class Solution:
    def minMaxDifference(self, num: int) -> int:
        ss = str(num)
        minimum = ss.replace(ss[0], '0')
        for ch in ss:
            if ch != '9':
                maximum = ss.replace(ch, '9')
                break
        else:
            maximum = ss
        return int(maximum) - int(minimum)


if __name__ == '__main__':
    solution = Solution().minMaxDifference(11891)
    print(solution)
