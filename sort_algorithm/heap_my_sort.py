# -*- coding: UTF-8 -*- 
# created by shenjiannan 2020-09-26 10:57

import random
from math import log, ceil, pi
# from loguru import logger


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


def heap_sort_my(ln):
    """
    建堆的时候自己实现的，使用了python中，math模块的log函数，用来找到这个堆一共有多少层。
    视频里面的方法没有用log函数
    堆排序 时间复杂度：n*log(n)
    :param ln: 传入的列表
    :return:
    """
    print('len(ln):', len(ln))
    # n = ((len(ln) - 1) // 2) - 1 # 从0开始算
    n = ceil(log(len(ln), 2)) - 1
    print("共有{}层".format(n))
    high = len(ln) - 1
    # 1, 建堆 （这个堆满足大堆根的条件）
    # n-1 次循环， 从倒数第二层开始循环，每一次循环做一次向下调整
    for i in range(n-1, -1, -1):
        print("正在处理第{}层。。。".format(i))
        # i 是表示二叉树的层数，从倒数第2层开始循环
        # 上一层的最后一个元素的位置：2**n - 1
        for j in range(2**i - 1, 2**i+2**i):
            print('j:', j)
            sift(ln, j, high)
    print(ln)

    # 2,此时堆定是最大的元素，让堆顶元素和二叉树最后一个元素交换位置
    # ln[0], ln[len(ln) - 1] = ln[len(ln) - 1], ln[0]
    # 3，做一次向下调整,此时high表示的位置就不是最后一个了，是最后一个位置减去1
    # sift(ln, 0, len(ln) - 1 - 1)
    # 4,重复第3步， 直到 low 和 high相等，即都是0
    high = len(ln) - 1
    while high > 0:
        ln[0], ln[high] = ln[high], ln[0]
        high = high - 1
        sift(ln, 0, high)


def heap_sort_normal(ln):
    """
    建堆的过程先找到最后一个元素的父节点，然后从这个父节点开始，依次往前遍历
    :param ln:
    :return:
    """
    # 1,最后一个元素位置
    n = len(ln) - 1
    # 2，最后一个元素的父节点位置
    last_father_pos = (n - 1) // 2
    # 从last_father_pos位置开始往前遍历，遍历到第一个节点，堆每个节点调用sift函数，每个节点就是根顶元素
    for i in range(last_father_pos, -1, -1):
        # 传入sift的high值，可以用列表ln最后一个元素，就可以满足条件，不需要用每一个二叉树的最后一个节点位置
        sift(ln, i, n)

    # 3,此时堆定是最大的元素，让堆顶元素和二叉树最后一个元素交换位置
    # ln[0], ln[len(ln) - 1] = ln[len(ln) - 1], ln[0]
    # 4，做一次向下调整,此时high表示的位置就不是最后一个了，是最后一个位置减去1
    # sift(ln, 0, len(ln) - 1 - 1)
    # 5,重复第4步， 直到 low 和 high相等，即都是0
    high = len(ln) - 1
    while high > 0:
        ln[0], ln[high] = ln[high], ln[0]
        high = high - 1
        sift(ln, 0, high)


if __name__ == '__main__':
    # ln = [6, 9, 8, 11, 5, 5, 3, 15, 18, 567,0,-6,-89,1111,56,21]
    l = [1, 10, 4, 5, 2, 8]
    # sift(ln, 0, 1)
    # heap_sort_my(l)
    heap_sort_normal(l)
    print(l)
