#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-19 23:07
FileName: P2600. K 件物品的最大和
Description:
"""


class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        nums = [*[1] * numOnes, *[0] * numZeros, *[-1] * numNegOnes]
        return sum(nums[:k])


if __name__ == '__main__':
    solution = Solution().kItemsWithMaximumSum(numOnes=3, numZeros=2, numNegOnes=0, k=2)
    print(solution)
