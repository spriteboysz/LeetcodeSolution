#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-07 22:41
FileName: P0596. 超过 5 名学生的课
Description:
"""

import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    s = courses['class'].value_counts()
    return s[s >= 5].reset_index()[['class']]


if __name__ == '__main__':
    data = [['A', 'Math'], ['B', 'English'], ['C', 'Math'], ['D', 'Biology'], ['E', 'Math'], ['F', 'Computer'],
            ['G', 'Math'], ['H', 'Math'], ['I', 'Math']]
    courses = pd.DataFrame(data, columns=['student', 'class']).astype({'student': 'object', 'class': 'object'})
    rs = find_classes(courses)
    print(rs)
