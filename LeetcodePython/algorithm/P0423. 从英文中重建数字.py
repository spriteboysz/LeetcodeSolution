#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-09 23:48
FileName: P0423. 从英文中重建数字
Description:
"""
from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        counter = Counter(s)
        n0, n2, n4, n6, n8 = counter['z'], counter['w'], counter['u'], counter['x'], counter['g']
        n1, n3, n5, n7 = counter['o'] - n4 - n0 - n2, counter['h'] - n8, counter['f'] - n4, counter['s'] - n6
        n9 = counter['i'] - n5 - n6 - n8
        return "".join(i * j for i, j in zip('0123456789', [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]))


if __name__ == '__main__':
    solution = Solution().originalDigits(s="owoztneoer")
    print(solution)
