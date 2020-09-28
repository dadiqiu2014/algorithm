# -*- coding: UTF-8 -*- 
# created by shenjiannan 2020-09-28 14:06
import random


def sift(ln, low, high):
    """
    实现小根堆的一次向下调整
    :param ln:
    :param low:
    :param high:
    :return:
    """
    tmp = ln[low]
    i = low
    j = 2*i + 1

    while j <= high:
        if j + 1 <= high and ln[j+1] < ln[j]:
            j = j + 1

        if ln[j] < tmp:
            ln[i] = ln[j]
            i = j
            j = 2*i + 1
        else:
            break
    ln[i] = tmp


def top_k(ln, k):
    """
    在列表ln中，取出前k个最大的数
    使用堆排序的方式实现
    时间复杂度 n*log(k)
    :param ln: 传入的元素列表
    :param k: 取出前k个最大的数
    :return:
    """
    # 1, 取ln中前k个数，建立一个小根堆
    heap = ln[:k]
    # 2,heap中，最后一个父节点的位置
    last_father_pos = (k - 2) // 2
    for i in range(last_father_pos, -1, -1):
        sift(heap, i, k-1)
    # 此时的列表ln中前k个元素小根堆已经建好了
    print(heap)
    # 3，堆顶是最小元素, 和最后一个位置元素互换
    for i in ln[k:]:
        if i > heap[0]:
            heap[0] = i
            sift(heap, 0, k-1)
    # 此时的堆就是列表ln中前k个最大元素
    print('heap:', heap)
    # 4，按顺序输出
    while k > 0:
        heap[0], heap[k-1] = heap[k-1], heap[0]
        k = k - 1
        sift(heap, 0, k-1)
    print(heap)


if __name__ == '__main__':
    l = [3, 5, 9, 1, 4, 2, 1, 100 , 200, 43]
    print(l)
    top_k(l, 4)
