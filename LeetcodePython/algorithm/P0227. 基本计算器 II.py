#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-08 23:00
FileName: P0227. 基本计算器 II
Description:
"""
import re
from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '').replace('-', '+-')
        stack = []
        for el in s.split('+'):
            if '*' in el or '/' in el:
                nums = re.split(r'[*|/]', el)
                queue = deque(nums)
                tokens = re.findall(r'[*|/]', el)
                for token in tokens:
                    a, b = int(queue.popleft()), int(queue.popleft())
                    if token == '*':
                        queue.appendleft(a * b)
                    else:
                        queue.appendleft(int(a / b))
                stack.append(queue[0])
            else:
                stack.append(int(el))
        return sum(stack)


if __name__ == '__main__':
    solution = Solution().calculate(s="14-3/2")
    print(solution)
