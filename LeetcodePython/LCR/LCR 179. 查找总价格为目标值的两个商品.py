#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-21 19:59
FileName: LCR 179. 查找总价格为目标值的两个商品
Description:
"""
from collections import Counter
from typing import List


class Solution:
    def twoSum(self, price: List[int], target: int) -> List[int]:
        counter = Counter(price)
        for k, v in counter.items():
            if target - k not in counter:
                continue
            if target - k == k:
                if v >= 2:
                    return [k, k]
            else:
                return [k, target - k]
        return [-1, -1]


if __name__ == '__main__':
    solution = Solution().twoSum(price=[8, 21, 27, 34, 52, 66], target=61)
    print(solution)
