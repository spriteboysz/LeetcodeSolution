#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-12 23:06
FileName: P1404. 将二进制表示减到 1 的步骤数
Description:
"""

from icecream import ic


class Solution:
    def numSteps(self, s: str) -> int:
        def calc(s):
            ss, s, carry = [], list(s), 1
            while s or carry:
                if s:
                    carry += int(s.pop())
                carry, mod = divmod(carry, 2)
                ss.append(str(mod))
            return ''.join(ss)[::-1]

        cnt = 0
        while s != '1':
            if s.endswith('0'):
                ss = s.rstrip('0')
                cnt += len(s) - len(ss)
                s = ss
            else:
                s = calc(s)
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().numSteps('1101')
    ic(solution)
