#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 16:13
FileName: LC/LCR 148. 验证图书取出顺序.py
Description: 
"""
from collections import deque
from typing import List


class Solution:
    def validateBookSequences(self, putIn: List[int], takeOut: List[int]) -> bool:
        stack = []
        queue = deque(takeOut)
        for num in putIn:
            stack.append(num)
            while stack and queue and stack[-1] == queue[0]:
                stack.pop()
                queue.popleft()
        return not stack and not queue


if __name__ == '__main__':
    solution = Solution().validateBookSequences(
        putIn=[6, 7, 8, 9, 10, 11],
        takeOut=[9, 11, 10, 8, 7, 6]
    )
    print(solution)
