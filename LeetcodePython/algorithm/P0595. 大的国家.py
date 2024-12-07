#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-07 22:33
FileName: P0595. 大的国家
Description:
"""

import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world.loc[(world['area'] >= 3000000) | (world['population'] >= 25000000), ['name', 'area', 'population']]


if __name__ == '__main__':
    data = [
        ['Afghanistan', 'Asia', 652230, 25500100, 20343000000],
        ['Albania', 'Europe', 28748, 2831741, 12960000000],
        ['Algeria', 'Africa', 2381741, 37100000, 188681000000],
        ['Andorra', 'Europe', 468, 78115, 3712000000],
        ['Angola', 'Africa', 1246700, 20609294, 100990000000]
    ]
    world = pd.DataFrame(
        data,
        columns=['name', 'continent', 'area', 'population', 'gdp']
    ).astype(
        {'name': 'object', 'continent': 'object', 'area': 'Int64', 'population': 'Int64', 'gdp': 'Int64'}
    )
    rs = big_countries(world)
    print(rs)
