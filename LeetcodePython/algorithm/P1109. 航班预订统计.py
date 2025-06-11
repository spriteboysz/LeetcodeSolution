#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-06-10 23:08
FileName: algorithm/P1109. 航班预订统计.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)
        for left, right, num in bookings:
            diff[left - 1] += num
            diff[right] -= num
        seats = [0] * n
        seats[0] = diff[0]
        for i in range(1, n):
            seats[i] = seats[i - 1] + diff[i]
        return seats


if __name__ == '__main__':
    solution = Solution().corpFlightBookings(bookings=[[1, 2, 10], [2, 3, 20], [2, 5, 25]], n=5)
    ic(solution)
