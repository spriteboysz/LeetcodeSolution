#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-08 23:27
FileName: P1003. 检查替换后的词是否有效
Description:
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == 'c':
                if len(stack) < 2:
                    return False
                if stack[-2] == 'a' and stack[-1] == 'b':
                    stack.pop()
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return not stack


if __name__ == '__main__':
    solution = Solution().isValid("abcabcababcc")
    print(solution)
