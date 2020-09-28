import random
import time
from sort_algorithm.tool import time_dec

# todo: 完成快速排序算法


def quick_sort(ln):
    """
    快速排序
    1，找一个元素m，让比这个元素m小的元素放到它的左边，比这个元素大的元素放在它的右边
    2，将第1步封装成一个函数partition(ln, left ,right)，返回各个部分的left和right下标
    3，此时分成了两部分，比m元素小的部分，m, 比元素m大的部分
    4, 然后在对没有排好顺序的部分递归调用partition(ln, left ,right)
    :param ln:
    :return:
    """
    if len(ln) < 2:
        return ln
    else:
        partition(ln)
    pass


def partition(ln):
    """
    根据ln的下标left, 和 下标right， 进行分组
    :param ln:
    :param left:
    :param right:
    :return:
    """
    if len(ln) < 2:
        return ln
    else:
        flag = ln[0]
        # 把从ln[left+1], 到ln[right]的元素进行分组，比first大的放在右边，比first小的元素放在左边
        # 现在left,即左边第一个元素相当与空出来了
        less = [i for i in ln if i < flag]
        greater = [i for i in ln if i > flag]
        return partition(less) + [flag] + partition(greater)


@time_dec
def use_partition(ln):
    partition(ln)


if __name__ == '__main__':
    l = [i for i in range(10000)]
    random.shuffle(l)
    # print("l:", l)
    use_partition(l)




