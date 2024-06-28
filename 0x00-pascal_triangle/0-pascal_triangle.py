#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(n):
    """
    pascal function
    """

    mlist = []

    if n <= 0:
        return mlist

    for i in range(n):
        rlist = []
        for y in range(i + 1):
            if (y == 0) or (y == i):
                val = 1
            else:
                val = mlist[i-1][y] + mlist[i-1][y-1]
            rlist.append(val)
        mlist.append(rlist)

    return mlist
