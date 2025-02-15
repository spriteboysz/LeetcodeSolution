#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-15 16:46
FileName: P3324. 出现在屏幕上的字符串序列
Description:
"""
from typing import List

from icecream import ic


class Solution:
    def stringSequence(self, target: str) -> List[str]:
        sequence = ['']
        for ch in target:
            sequence.extend([f'{sequence[-1]}{chr(c)}' for c in range(ord('a'), ord(ch) + 1)])
        return sequence[1:]


if __name__ == '__main__':
    solution = Solution().stringSequence(target="he")
    ic(solution)
