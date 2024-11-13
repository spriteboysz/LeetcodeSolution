#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-13 22:14
FileName: P1021. 删除最外层的括号
Description:
"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack, ss, start = [], '', 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(ch)
            else:
                stack.pop()
            if not stack:
                ss += s[start + 1:i]
                start = i + 1
        return ss


if __name__ == '__main__':
    solution = Solution().removeOuterParentheses(s="(()())(())")
    print(solution)
