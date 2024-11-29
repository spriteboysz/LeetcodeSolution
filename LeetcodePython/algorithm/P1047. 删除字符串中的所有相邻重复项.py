#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-29 21:23
FileName: P1047. 删除字符串中的所有相邻重复项
Description:
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for ch in s:
            if not stack:
                stack.append(ch)
            elif stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)


if __name__ == '__main__':
    solution = Solution().removeDuplicates("abbaca")
    print(solution)
