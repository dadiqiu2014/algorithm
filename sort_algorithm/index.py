# -*- coding: UTF-8 -*- 
# created by shenjiannan 2020-09-26 16:36

import random
from loguru import logger


def sift(ln, low, high):
    """
    实现一次向下调整过程
    前提：当前二叉树子节点都是大根堆，即满足条件：父节点的比子节点大
    调整完成后，使整个二叉树符合大根堆的特征
    :param ln:
    :param low: 要进行向下调整的二叉树的根节点的位置
    :param high: 二叉树最后一个节点的位置
    :return:
    """
    print('ln:', ln)
    print('low:', low)
    # 记录这个子二叉树根节点的值
    tmp = ln[low]
    # 当前空出来的位置，即需要在此位置上放上子节点，以使之符合大根堆的条件
    i = low
    # i是父节点的位置，那么它的子节点中，左边的那个子节点就是 2*i+1，如果有右子节点的话，就是2*i+2
    j = 2*i + 1

    # 循环条件：必须保证子节点的位置必须小于二叉树最后一个元素的位置
    while j <= high:
        # 比较i位置元素的两个子节点哪个大，选择大的哪个元素的位置作为j,前提是保证j+1这个位置存在
        if j + 1 <= high and ln[j] < ln[j + 1]:
            j = j + 1
        # 如果j位置的值大于tmp，那么就将j位置的值放到i位置上
        if ln[j] > tmp:
            ln[i] = ln[j]
            # 让i指向的位置变成j
            i = j
            # j为新的下一层的位置
            j = 2 * i + 1
        else:
            break
    ln[i] = tmp


def heap_sort(ln):
    """
    堆排序 时间复杂度：n*log(n)
    :param ln: 传入的列表
    :return:
    """
    n = (len(ln) - 1) // 2
    print("共有{}层".format(n))
    high = len(ln) - 1
    # 1, 建堆 （这个堆满足大堆根的条件）
    # n-1 次循环， 从倒数第二层开始循环，每一次循环做一次向下调整
    for i in range(n-1, -1, -1):
        print("正在处理第{}层。。。".format(i))
        # i 是表示二叉树的层数，从倒数第2层开始循环
        # 上一层的最后一个元素的位置：2**n - 1
        for j in range(2**i - 1, 2**i+2**i):
            sift(ln, j, high)
    print(ln)


if __name__ == '__main__':
    ln = [6, 9, 8, 11, 5, 3, 15, 18, 21]
    print(ln)
    # sift(ln, 0, 1)
    heap_sort(ln)
    print(ln)
