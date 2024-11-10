#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-10 16:46
FileName: P0020. 有效的括号
Description:
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = ['*']
        dic = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in dic:
                if stack[-1] == dic.get(ch):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return len(stack) == 1


if __name__ == '__main__':
    solution = Solution().isValid(s="()[]{}")
    print(solution)
