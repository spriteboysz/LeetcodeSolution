#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-29 21:05
FileName: P1614. 括号的最大嵌套深度
Description:
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        maximum, stack = 0, []
        for ch in s:
            if ch == '(':
                stack.append(ch)
                maximum = max(maximum, len(stack))
            elif ch == ')':
                stack.pop()
        return maximum


if __name__ == '__main__':
    solution = Solution().maxDepth(s="(1+(2*3)+((8)/4))+1")
    print(solution)
