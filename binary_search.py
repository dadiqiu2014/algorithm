# 二分查找
from math import floor


def binary_search(l, member):
    """
    通过二分查找，返回给定元素member在列表l中的位置。
    如果没有查到，那么返回-1
    :param l:
    :param member:
    :return:
    """
    # 如果需要查找的元素member 大于 列表中的最大元素或者小于列表中的最小元素，返回-1
    if member > l[-1] or member < l[0]:
        return -1
    left = 0
    right = len(l)
    while left <= right:
        mid = floor((left + right) / 2)
        if l[mid] > member:
            right = mid - 1
        elif l[mid] < member:
            left = mid + 1
        else:
            return mid

    return -1


if __name__ == '__main__':
    l1 = [1, 2, 3, 4, 5, 8, 20, 25, 28, 89, 102, 105]
    print(binary_search(l1, 1000))
