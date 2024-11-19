#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-19 22:55
FileName: P2566. 替换一个数字后的最大差值
Description:
"""


class Solution:
    def minMaxDifference(self, num: int) -> int:
        ss = str(num)
        minimum = int(ss.replace(ss[0], '0'))
        digit = [d for d in ss if d != '9']
        d = digit[0] if digit else 'x'
        maximum = int(ss.replace(d, '9'))
        return maximum - minimum


if __name__ == '__main__':
    solution = Solution().minMaxDifference(99999)
    print(solution)
