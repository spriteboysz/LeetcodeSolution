#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-05 16:48
FileName: LCP/P0946. 验证栈序列.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped = popped[1:]
        return not stack


if __name__ == '__main__':
    solution = Solution().validateStackSequences(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1])
    ic(solution)
