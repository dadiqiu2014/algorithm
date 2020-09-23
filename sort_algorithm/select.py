import random

"""选择排序, 时间复杂度：n^2"""


def select_sort_simple(ln):
    """
    简单的选择排序，使用python内置的辅助函数
    :param ln:
    :return:
    """
    # 用一个新的列表来存放排好顺序的元素
    new_list = []

    # 遍历原列表
    for i in range(len(ln)):
        # 获取列表中最小的元素
        min_element = min(ln)
        # 将最小元素插入到新列表
        new_list.append(min_element)
        # 删除最小元素
        ln.remove(min_element)

    return new_list


def select_sort(ln):
    """
    本地排序(不借助额外容器存储元素)，不实用内置python方法
    :param ln:
    :return:
    """
    # 每一次选择一个最小的元素，这个选择最小元素的过程成为一趟，共需要 (列表长度-1) 趟
    # 每趟选择出的最小元素和无顺序区的第一个元素交换位置
    # 每趟之后，有顺序区的长度加1，无顺序区的长度减一
    # 第i趟时，有序区的范围是ln[:i], 无序区的范围是ln[i:]
    for i in range(len(ln) - 1):
        # 记录每趟最小元素的位置，循环开始时认为是第一个元素
        min_loc = i
        for j in range(i + 1, len(ln)):
            if ln[j] < ln[min_loc]:
                min_loc = j
        ln[i], ln[min_loc] = ln[min_loc], ln[i]
    return ln


if __name__ == '__main__':
    l = [random.randint(0, 100) for _ in range(10)]
    print(l)
    # print(select_sort_simple(l))
    print(select_sort(l))

