#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-11 21:49
FileName: P0412. Fizz Buzz
Description:
"""
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append('FizzBuzz')
            elif i % 3 == 0:
                ans.append('Fizz')
            elif i % 5 == 0:
                ans.append('Buzz')
            else:
                ans.append(str(i))
        return ans


if __name__ == '__main__':
    solution = Solution().fizzBuzz(6)
    print(solution)
