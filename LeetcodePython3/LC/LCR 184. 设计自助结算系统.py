#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 15:22
FileName: LC/LCR 184. 设计自助结算系统.py
Description: 
"""


class Checkout:

    def __init__(self):
        pass

    def get_max(self) -> int:
        pass

    def add(self, value: int) -> None:
        pass

    def remove(self) -> int:
        pass


if __name__ == '__main__':
    checkout = Checkout()
    checkout.add(4)
    checkout.add(7)
    print(checkout.get_max())
    print(checkout.remove())
    print(checkout.get_max())
