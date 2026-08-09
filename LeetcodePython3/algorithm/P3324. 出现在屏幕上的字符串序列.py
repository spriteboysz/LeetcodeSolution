#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-09 18:53
FileName: P3324. 出现在屏幕上的字符串序列.py
Description:
"""
from typing import List


class Solution:
    def stringSequence(self, target: str) -> List[str]:
        sequence = ['']
        for ch in target:
            path = [chr(i) for i in range(ord('a'), ord(ch) + 1)]
            sequence.extend([f'{sequence[-1]}{c}' for c in path])
        return sequence[1:]


if __name__ == '__main__':
    solution = Solution().stringSequence(target="he")
    print(solution)
