#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-07 09:25
FileName: 面试题/LCR 037. 行星碰撞.py
Description: 
"""
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for aster in asteroids:
            alive = True
            while alive and aster < 0 and stack and stack[-1] > 0:
                alive = stack[-1] < -aster
                if stack[-1] <= -aster:
                    stack.pop()
            if alive:
                stack.append(aster)
        return stack



if __name__ == '__main__':
    solution = Solution().asteroidCollision([10, 2, -5])
    print('<None>' if not solution else f'{solution=}')
