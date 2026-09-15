#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-14 15:13
FileName: algorithm/P3606. 优惠券校验器.py
Description: 
"""
import re
from typing import List


class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        validate = []
        pattern = re.compile(r'^\w+$')
        seen = {'electronics', 'grocery', 'pharmacy', 'restaurant'}
        for c, b, a in zip(code, businessLine, isActive):
            if pattern.match(c) and b in seen and a is True:
                validate.append((c, b))
        validate.sort(key=lambda v: (v[1], v[0]))
        return [v[0] for v in validate]


if __name__ == '__main__':
    solution = Solution().validateCoupons(
        code=['SAVE20', '', 'PHARMA5', 'SAVE@20'],
        businessLine=['restaurant', 'grocery', 'pharmacy', 'restaurant'],
        isActive=[True, True, True, True]
    )
    print('<None>' if solution is None else f'{solution=}')
