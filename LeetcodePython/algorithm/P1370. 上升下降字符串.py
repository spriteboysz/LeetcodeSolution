#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-04 18:06
FileName: P1370. 上升下降字符串
Description:
"""

from collections import Counter

from icecream import ic


class Solution:
    def sortString(self, s: str) -> str:
        counter = Counter(s)
        ans, n, ss = [], len(s), sorted(counter)
        while n:
            for ch in ss:
                if counter.get(ch, 0) > 0:
                    ans.append(ch)
                    n -= 1
                    counter[ch] -= 1
            for ch in ss[::-1]:
                if counter.get(ch, 0) > 0:
                    ans.append(ch)
                    n -= 1
                    counter[ch] -= 1
        return ''.join(ans)


if __name__ == '__main__':
    solution = Solution().sortString("aaaabbbbcccc")
    ic(solution)
