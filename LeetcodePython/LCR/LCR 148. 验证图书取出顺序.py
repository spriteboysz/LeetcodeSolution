#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-03 21:22
FileName: LCR 148. 验证图书取出顺序
Description:
"""
from typing import List


class Solution:
    def validateBookSequences(self, putIn: List[int], takeOut: List[int]) -> bool:
        stack, pos = [], 0
        for num in putIn:
            stack.append(num)
            while stack and stack[-1] == takeOut[pos]:
                stack.pop()
                pos += 1
        return not stack and pos == len(takeOut)


if __name__ == '__main__':
    solution = Solution().validateBookSequences(putIn=[6, 7, 8, 9, 10, 11], takeOut=[9, 11, 10, 8, 7, 6])
    print(solution)
