#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-02-28 22:41
FileName: P3827. 统计单比特整数.py
Description:
"""

import math

class Solution:
    def countMonobit(self, n: int) -> int:
        return int(math.log(n + 1, 2)) + 1


if __name__ == '__main__':
    s = Solution().countMonobit(7)
    print(s)
