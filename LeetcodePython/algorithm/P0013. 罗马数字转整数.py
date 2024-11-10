#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 09:44
FileName: P0013. 罗马数字转整数
Description:
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        tran1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        tran2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        total = 0
        while s:
            if s[:2] in tran2:
                total += tran2.get(s[:2])
                s = s[2:]
            elif s[0] in tran1:
                total += tran1.get(s[0])
                s = s[1:]
            else:
                raise ValueError('Error')
        return total


if __name__ == '__main__':
    solution = Solution().romanToInt(s="I")
    print(solution)
