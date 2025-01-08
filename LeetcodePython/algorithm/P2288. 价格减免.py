#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-08 20:53
FileName: P2288. 价格减免
Description:
"""

from icecream import ic


class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.strip().split()
        for i, word in enumerate(words):
            if word[0] == '$' and word[1:].isdigit():
                words[i] = f'${int(word[1:]) * (100 - discount) / 100:.2f}'
        return ' '.join(words)


if __name__ == '__main__':
    solution = Solution().discountPrices(sentence="there are $1 $2 and 5$ candies in the shop", discount=50)
    ic(solution)
