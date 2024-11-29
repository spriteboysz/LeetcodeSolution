#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-29 21:01
FileName: P2696. 删除子串后的字符串最小长度
Description:
"""


class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for ch in s:
            if stack and stack[-1] == 'A' and ch == 'B':
                stack.pop()
            elif stack and stack[-1] == 'C' and ch == 'D':
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)


if __name__ == '__main__':
    solution = Solution().minLength(s="ABFCACDB")
    print(solution)
