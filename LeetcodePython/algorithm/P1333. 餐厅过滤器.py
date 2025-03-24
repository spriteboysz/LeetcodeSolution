#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-23 21:43
FileName: algorithm/P1333. 餐厅过滤器.py
Description: 
"""
from typing import List

from icecream import ic


class Solution:
    def filterRestaurants(self, restaurants, veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        results = []
        for id_, rating, vegan_friendly, price, distance in restaurants:
            if veganFriendly and vegan_friendly != veganFriendly:
                continue
            if price > maxPrice:
                continue
            if distance > maxDistance:
                continue
            results.append((id_, rating))
        return [id_ for id_, _ in sorted(results, key=lambda el: (-el[1], -el[0]))]


if __name__ == '__main__':
    solution = Solution().filterRestaurants(
        restaurants=[[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]],
        veganFriendly=1,
        maxPrice=50,
        maxDistance=10)
    ic(solution)
