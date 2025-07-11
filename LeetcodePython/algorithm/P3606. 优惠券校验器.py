#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-07-11 21:15
FileName: algorithm/P3606. 优惠券校验器.py
Description: 
"""
from typing import List

from icecream import ic
from string import ascii_letters, digits


class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        actives = []
        ss = '_' + ascii_letters + digits
        for num, business, active in zip(code, businessLine, isActive):
            if not num:
                continue
            if [n for n in num if n not in ss]:
                continue
            if business not in {'electronics', 'grocery', 'pharmacy', 'restaurant'}:
                continue
            if not active:
                continue
            actives.append((business, num))
        return [el[1] for el in sorted(actives)]


if __name__ == '__main__':
    solution = Solution().validateCoupons(
        code=["SAVE20", "", "PHARMA5", "SAVE@20"],
        businessLine=["restaurant", "grocery", "pharmacy", "restaurant"],
        isActive=[True, True, True, True]
    )
    ic(solution)
