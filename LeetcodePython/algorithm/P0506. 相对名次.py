# ! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-22 22:55
FileName: P506. 相对名次
Description:
"""
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dic = [(num, i) for i, num in enumerate(score)]
        dic.sort(key=lambda el: el[0], reverse=True)
        dic2 = [(el[1], i) for i, el in enumerate(dic)]
        dic2.sort(key=lambda el: el[0])
        ranks = [str(el[1] + 1) for el in dic2]
        for i, rank in enumerate(ranks):
            if rank == '1':
                ranks[i] = 'Gold Medal'
            if rank == '2':
                ranks[i] = 'Silver Medal'
            if rank == '3':
                ranks[i] = 'Bronze Medal'
        return ranks


if __name__ == '__main__':
    solution = Solution().findRelativeRanks(score=[10, 3, 8, 9, 4])
    print(solution)
