#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-16 00:32
FileName: P1221. 分割平衡字符串.py
Description:
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack, cnt = [], 0
        for ch in s:
            if stack and stack[-1] != ch:
                stack.pop()
            else:
                stack.append(ch)
            cnt += int(not stack)
        return cnt


if __name__ == '__main__':
    solution = Solution().balancedStringSplit(s="RLRRRLLRLL")
    print(solution)
