#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-19 22:51
FileName: P1221. 分割平衡字符串
Description:
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        acc, num = 0, 0
        for ch in s:
            if ch == 'R':
                acc += 1
            else:
                acc -= 1
            if acc == 0:
                num += 1
        return num


if __name__ == '__main__':
    solution = Solution().balancedStringSplit("RLRRRLLRLL")
    print(solution)
