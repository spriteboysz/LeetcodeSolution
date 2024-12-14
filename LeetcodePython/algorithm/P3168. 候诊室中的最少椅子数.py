#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-13 21:44
FileName: P3168. 候诊室中的最少椅子数
Description:
"""


class Solution:
    def minimumChairs(self, s: str) -> int:
        maximum, stack = 0, []
        for ch in s:
            if ch == 'E':
                stack.append(1)
            else:
                stack.pop()
            maximum = max(maximum, sum(stack))
        return maximum


if __name__ == '__main__':
    solution = Solution().minimumChairs(s="ELELEEL")
    print(solution)
