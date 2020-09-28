import random
from pprint import pprint
from sort_algorithm.tool import time_dec

"""冒泡排序算法 时间负责度：n^2"""

# l = [random.randint(0, 101) for _ in range(10)]
# print(l)


def one_bubble(ln, n=0):
    """

    :param ln:
    :param n: 表示第几趟冒泡，m个元素的列表，需要m-1趟排序完毕
    :return:
    """
    count = len(ln)
    i = 0
    while i < count-1-n:
        if ln[i] > ln[i + 1]:
            ln[i], ln[i+1] = ln[i+1], ln[i]
        i += 1

    return ln


def bubble(ln):

    for i in range(len(ln)-1):
        # i 表示第几趟
        ln = one_bubble(ln, i)

    return ln


@time_dec
def sort_bubble(ln):
    """
    视频教程标准答案
    :param ln:
    :return:
    """
    # 第一层循环表示冒泡排序每一趟的操作
    for i in range(len(ln)-1):
        # 标志变量，用来记录本趟的操作是否有元素交换，如果没有，表示已经排好顺序了，退出循环
        exchange = False
        # 第二层循环表示每一趟要遍历的元素，每一趟遍历的元素比上一次要遍历的元素少一个
        for j in range(len(ln) - 1 - i):
            if ln[j] > ln[j + 1]:
                ln[j], ln[j + 1] = ln[j + 1], ln[j]
                exchange = True
        if exchange is False:
            return ln

    return ln


if __name__ == '__main__':
    # print(one_bubble(l))
    # print(bubble(l))
    # l2 = [random.randint(0, 101) for _ in range(10)]
    # print(l2)
    # print(sort_bubble(l2))
    l = [i for i in range(10000)]
    random.shuffle(l)
    sort_bubble(l)
