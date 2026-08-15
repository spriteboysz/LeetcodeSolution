#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-08-14 20:41
FileName: algorithm/P1418. 点菜展示表.py
Description: 
"""
from typing import List
from collections import defaultdict


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        dic = defaultdict(lambda: defaultdict(int))
        foods = set()
        for name, table, food in orders:
            dic[int(table)][food] += 1
            foods.add(food)

        foods = sorted(foods)
        tables = [['Table', *foods]]
        for table in sorted(dic):
            row = [str(table)]
            for food in foods:
                row.append(str(dic.get(table, {}).get(food, 0)))
            tables.append(row)
        return tables


if __name__ == '__main__':
    solution = Solution().displayTable(
        orders=[
            ["David", "3", "Ceviche"],
            ["Corina", "10", "Beef Burrito"],
            ["David", "3", "Fried Chicken"],
            ["Carla", "5", "Water"],
            ["Carla", "5", "Ceviche"],
            ["Rous", "3", "Ceviche"]
        ]
    )
    print(solution)
