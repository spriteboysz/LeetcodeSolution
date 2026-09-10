#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 13:20
FileName: LC/LCS 02. 完成一半题目.py
Description: 
"""
from collections import Counter

from typing import List


class Solution:
    def halfQuestions(self, questions: List[int]) -> int:
        counter = Counter(questions)
        question_type = sorted(counter, key=lambda q: -counter.get(q, 0))
        acc = 0
        for i, type_ in enumerate(question_type):
            acc += counter.get(type_, 0)
            if acc >= len(questions) // 2:
                return i + 1
        return -1


if __name__ == '__main__':
    solution = Solution().halfQuestions(questions=[1, 5, 1, 3, 4, 5, 2, 5, 3, 3, 8, 6])
    print('<None>' if not solution else f'{solution=}')
