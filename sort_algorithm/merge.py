# -*- coding: UTF-8 -*- 
# created by shenjiannan 2020-09-30 15:21


import random
import time
from sort_algorithm.tool import time_dec


def merge(l1, l2):
    """
    给两个有序列表，l1，l2, 合并它们，让他们依然有序
    :param l1:
    :param l2:
    :return:
    """
    new_list = []
    l1_pos = 0
    l2_pos = 0
    while l1_pos < len(l1) and l2_pos < len(l2):
        if l1[l1_pos] < l2[l2_pos]:
            new_list.append(l1[l1_pos])
            l1_pos += 1
        else:
            new_list.append(l2[l2_pos])
            l2_pos += 1
    # print('l1_pos:', l1_pos)
    # print('l2_pos:', l2_pos)
    if l1_pos == len(l1):
        new_list += l2[l2_pos:]
    elif l2_pos == len(l2):
        new_list += l1[l1_pos:]

    return new_list


def merge_sort(ln):
    """
    使用归并排序
    时间复杂度：n*log(n)
    :param ln:
    :return:
    """
    if len(ln) <= 1:
        return ln
    else:
        mid = len(ln) // 2
        l1 = merge_sort(ln[:mid])
        l2 = merge_sort(ln[mid:])
        return merge(l1, l2)


if __name__ == '__main__':
    # a = [1, 2, 3, 12]
    # b = [10, 15, 20]
    # print(merge(a, b))
    a = [random.randint(0, 100) for _ in range(10)]
    print(a)
    print(merge_sort(a))




