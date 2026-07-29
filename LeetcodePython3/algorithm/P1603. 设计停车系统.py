#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-28 23:02
FileName: P1603. 设计停车系统.py
Description:
"""


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parking = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.parking[carType - 1] == 0:
            return False
        self.parking[carType - 1] -= 1
        return True


if __name__ == '__main__':
    solution = ParkingSystem(1, 1, 0)
    print(solution)
