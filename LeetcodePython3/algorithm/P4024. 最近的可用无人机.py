#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-09 15:07
FileName: algorithm/P4024. 最近的可用无人机.py
Description: 
"""


class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        distances = []
        for x, y, d in drones:
            distances.append(abs(x - target[0]) + abs(y - target[1]))
        indexes = []
        for (i, drone), distance in zip(enumerate(drones), distances):
            if drone[2] >= distance:
                indexes.append(i)
        return min(((distance, i) for i, distance in enumerate(distances) if i in indexes), default=(-1, -1))[1]


if __name__ == '__main__':
    solution = Solution().nearestDrone(drones=[[0, 0, 8], [2, 2, 9]], target=[3, 4])
    print('<None>' if solution is None else f'{solution=}')
