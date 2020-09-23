# -*- coding: UTF-8 -*- 
# created by shenjiannan 2020-09-22 18:44

import random


def insert_sort(ln):
    """
    插入排序
    时间复杂度n^2
    1，初始状态，有序区为ln的第1个元素，无顺序区是从ln列表的第2个元素到最后一个元素
    2，把列表ln想象成扑克牌，有序区的元素是手里的牌，从小到大已经排好顺序，无顺序区的元素是放在桌子上的一堆儿牌
    3，每一次拿桌子上的那一堆牌的最上边一张
    4，用抽到的牌和手里的牌依次做比较，把抽到的牌按照顺讯放在合适的位置
    5，共需要摸牌 len(ln) - 1 次，也就是，把摸到的牌插入到正确的位置，这个操作也执行 len(ln) - 1 次
    :param ln:
    :return:
    """
    for i in range(1, len(ln)):
        # i 代表的是摸到的牌的下标，第一张牌不需要排序，所以从第二张牌开始
        # tmp为摸到的牌
        tmp = ln[i]
        # j 为有序区的一个位置，初始化为i-1，代表有序区的最后一张牌的位置
        j = i - 1
        while tmp < ln[j] and j >= 0:
            # 如果摸到的牌tmp比当前的牌ln[j]小，并且j>=0,
            # 让ln[j]这个元素向由移动一个位置
            ln[j + 1] = ln[j]
            # 因为ln[j]这张牌比摸到的大，所以j指向的位置前移
            j = j - 1
        # 如果tmp 比 ln[j]大，那么tmp放到ln[j]后面的位置
        ln[j+1] = tmp
        print('第%s次：%s' % (i, ln))


if __name__ == '__main__':
    l = [random.randint(1, 100) for _ in range(10)]
    print("初始状态:", l)
    insert_sort(l)
    print("最终结果：", l)