#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-24 11:45
FileName: P2037. 使每位学生都有座位的最少移动次数
Description:
"""
from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        return sum([abs(seat - student) for seat, student in zip(seats, students)])


if __name__ == '__main__':
    solution = Solution().minMovesToSeat(seats=[4, 1, 5, 9], students=[1, 3, 2, 6])
    print(solution)
