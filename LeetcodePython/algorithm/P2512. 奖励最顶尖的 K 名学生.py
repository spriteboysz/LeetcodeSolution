#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-04-26 16:28
FileName: algorithm/P2512. 奖励最顶尖的 K 名学生.py
Description: 
"""
from functools import lru_cache
from typing import List

from icecream import ic


class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str],
                    student_id: List[int], k: int) -> List[int]:
        positive, negative = set(positive_feedback), set(negative_feedback)

        @lru_cache
        def calc(info):
            words = info.split()
            score = 0
            for word in words:
                if word in positive:
                    score += 3
                elif word in negative:
                    score -= 1
            return score

        students = [(id_, r) for id_, r in zip(student_id, report)]
        return [id_ for id_, _ in sorted(students, key=lambda stu: (-calc(stu[1]), stu[0]))][:k]


if __name__ == '__main__':
    solution = Solution().topStudents(
        positive_feedback=["smart", "brilliant", "studious"],
        negative_feedback=["not"],
        report=["this student is studious", "the student is smart"],
        student_id=[1, 2],
        k=2)
    ic(solution)
