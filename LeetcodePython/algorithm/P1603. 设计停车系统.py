#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-06 22:36
FileName: algorithm/P1603. 设计停车系统.py
Description: 
"""

from icecream import ic


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.parking[carType] - 1 >= 0:
            self.parking[carType] -= 1
            return True
        return False


if __name__ == '__main__':
    solution = ParkingSystem(1, 1, 0)
    ic(solution.addCar(1))
    ic(solution.addCar(2))
    ic(solution.addCar(3))
    ic(solution.addCar(1))
