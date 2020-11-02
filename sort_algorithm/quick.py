# -*- coding: UTF-8 -*- 
# created by shenjiannan 2020-09-24 16:00

import random


def partition(ln, left, right):
    """
    给定一个列表，给定左右下标left和right，对ln[left:right]进行元素位置移动，最后让ln[left]在这个ln[left:right]中间的位置，使其左边的元素都比它小，右边的元素都比它大
    :param ln: 原始的需要排序的列表
    :param left: 左边开始的位置
    :param right: 右边开始的位置
    :return: 返回一个位置mid, mid左边的元素都比mid位置的元素小， mid右边的元素都比mid位置的元素da
    """
    tmp = ln[left]
    while left < right:
        while left < right and ln[right] >= tmp:
            # 如果ln[right]的值比tmp大,那么让right指向的位置减1
            right = right - 1
        # 此时，right位置的元素是小于tmp的， 把这个元素复制到left位置上
        ln[left] = ln[right]

        while left < right and ln[left] <= tmp:
            # 如果ln[left] 的值比tmp小，那么让left指向的位置加1
            left = left + 1
        # 此时ln[left]的值比tmp大， 把这个元素复制到right位置上
        ln[right] = ln[left]

    # 此时，left的位置和right位置重合，把tmp复制到left位置上
    ln[left] = tmp

    return left


def quick_sort_my(ln, left, right):
    """
    快速排序 平均时间复杂度n*log(n) 最坏情况 n^2
    :param ln:
    :param left:
    :param right
    :return:
    """
    print('ln:', ln)
    # 如果ln长度小于2
    if len(ln[left:right]) <= 2:
        partition(ln, left, right)
    else:
        # 找中间位置
        mid = (left + right) // 2
        print('mid:', mid, 'left:', left, 'right:', right)
        # 递归执行
        quick_sort(ln, left, mid)
        quick_sort(ln, mid, right)


def quick_sort(ln, left, right):
    """

    :param ln:
    :param left:
    :param right:
    :return:
    """
    if left < right:
        mid = partition(ln, left, right)
        quick_sort(ln, left, mid-1)
        quick_sort(ln, mid+1, right)


if __name__ == '__main__':
    l = [5, 9, 4, 2, 1, 3]
    # mid = partition(l, 0, len(l)-1)
    # print(l)
    # print(mid)
    quick_sort(l, 0, len(l)-1)
    print(l)
