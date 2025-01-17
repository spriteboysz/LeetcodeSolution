#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-16 23:49
FileName: P1418. 点菜展示表
Description:
"""
from collections import defaultdict
from typing import List

from icecream import ic


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        dic = defaultdict(lambda: defaultdict(int))
        foods, ids = set(), set()
        for _, no, food in orders:
            dic[int(no)][food] += 1
            foods.add(food)
            ids.add(int(no))
        foods = sorted(foods)
        table = [['Table', *foods]]
        for no in sorted(ids):
            row = [str(no), *[str(dic.get(no).get(food, 0)) for food in foods]]
            table.append(row.copy())
        return table


if __name__ == '__main__':
    solution = Solution().displayTable(
        [["David", "3", "Ceviche"],
         ["Corina", "10", "Beef Burrito"],
         ["David", "3", "Fried Chicken"],
         ["Carla", "5", "Water"],
         ["Carla", "5", "Ceviche"],
         ["Rous", "3", "Ceviche"]])
    ic(solution)
