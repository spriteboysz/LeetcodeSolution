#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-06-10 22:55
FileName: algorithm/P2043. 简易银行系统.py
Description: 
"""
from typing import List

from icecream import ic


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > len(self.balance) or account2 > len(self.balance):
            return False
        if self.balance[account1 - 1] >= money:
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account > len(self.balance):
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > len(self.balance):
            return False
        if self.balance[account - 1] >= money:
            self.balance[account - 1] -= money
            return True
        return False


if __name__ == '__main__':
    bank = Bank([92, 62, 12, 81, 77, 38, 71, 8, 42, 38])
    ic(bank.transfer(3, 2, 18))
    ic(bank.transfer(29, 3, 99))
    ic(bank.deposit(8, 97))
