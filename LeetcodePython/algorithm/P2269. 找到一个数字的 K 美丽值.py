#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-08 22:27
FileName: P2269. 找到一个数字的 K 美丽值
Description:
"""

from icecream import ic


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ss = str(num)
        cnt = 0
        for i in range(len(ss) - k + 1):
            if (n := int(ss[i:i + k])) != 0 and num % n == 0:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().divisorSubstrings(num=430043, k=2)
    ic(solution)
