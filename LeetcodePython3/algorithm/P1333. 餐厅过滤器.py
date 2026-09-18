#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-17 14:05
FileName: algorithm/P1333. 餐厅过滤器.py
Description: 
"""
from typing import List


class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> \
    List[int]:
        def check(r):
            _, _, v, p, d = r
            if veganFriendly and not v:
                return False
            if p > maxPrice:
                return False
            if d > maxDistance:
                return False
            return True

        restaurants = [restaurant for restaurant in restaurants if check(restaurant)]
        restaurants.sort(key=lambda r: (-r[1], -r[0]))
        return [id_ for id_, *_ in restaurants]


if __name__ == '__main__':
    solution = Solution().filterRestaurants(
        restaurants=[
            [1, 4, 1, 40, 10],
            [2, 8, 0, 50, 5],
            [3, 8, 1, 30, 4],
            [4, 10, 0, 10, 3],
            [5, 1, 1, 15, 1]
        ],
        veganFriendly=1,
        maxPrice=50,
        maxDistance=10
    )
    print('<None>' if solution is None else f'{solution=}')
