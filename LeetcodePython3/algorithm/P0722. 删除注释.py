#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-20 22:54
FileName: P0722. 删除注释.py
Description:
"""
import re
from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        pattern = re.compile(r'/\*[\S\s]*?\*/|//.*')
        text = '\n'.join(source)
        text = pattern.sub('', text)
        return [line for line in text.splitlines() if line]


if __name__ == '__main__':
    solution = Solution().removeComments(
        source=["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;",
                "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
    )
    print(solution)
