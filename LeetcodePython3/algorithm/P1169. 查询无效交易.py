#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-02 22:41
FileName: algorithm/P1169. 查询无效交易.py
Description: 
"""
from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions = [transaction.split(',') for transaction in transactions]
        invalid = []
        for i, v in enumerate(transactions):
            if int(v[2]) > 1000:
                invalid.append(','.join(v))
                continue
            for j, u in enumerate(transactions):
                if i == j:
                    continue
                if v[0] == u[0] and v[3] != u[3] and abs(int(v[1]) - int(u[1])) <= 60:
                    invalid.append(','.join(v))
                    break
        return invalid


if __name__ == '__main__':
    solution = Solution().invalidTransactions([
        'alice,20,800,mtv',
        'alice,50,100,beijing',
        'bob,50,1200,mtv'
    ])
    print(solution)
