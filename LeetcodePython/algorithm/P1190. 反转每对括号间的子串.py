#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-06-10 23:17
FileName: algorithm/P1190. 反转每对括号间的子串.py
Description: 
"""

from icecream import ic


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack, left = [], []
        for ch in s:
            if ch == '(':
                left.append(len(stack))
            elif ch == ')':
                stack[left[-1]:] = stack[left[-1]:][::-1]
                left.pop()
            else:
                stack.append(ch)
        return ''.join(stack)


if __name__ == '__main__':
    solution = Solution().reverseParentheses(s="(ed(et(oc))el)")
    ic(solution)
