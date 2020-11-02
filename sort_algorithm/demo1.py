# -*- coding: UTF-8 -*- 
# created by shenjiannan 2020-10-19 15:20


class Deque:
    def __init__(self, str1):
        self.data = []
        self._add_items(str1)

    def _add_items(self, str1):
        for i in str1:
            self.data.append(i)

    def pop_front(self):
        return self.data.pop()

    def pop_end(self):
        return self.data.pop(0)

    @property
    def judge(self):
        f = None
        e = None
        flag = True
        while f == e and len(self.data) > 1:
            f = self.pop_front()
            e = self.pop_end()
            if f != e:
                flag = False

        return flag


def partition(ln, left, right):
    """

    :param ln:
    :param left:
    :param right:
    :return:
    """
    temp = ln[left]
    while left < right:
        while left < right and ln[right] > temp:
            right -= 1
        ln[left] = ln[right]
        while left < right and ln[left] < temp:
            left += 1
        ln[right] = ln[left]
    ln[left] = temp
    return left


def quick(ln, left, right):
    """

    :param ln:
    :param left:
    :param right:
    :return:
    """
    if left < right:
        mid = partition(ln, left, right)
        quick(ln, left, mid - 1)
        quick(ln, mid + 1, right)


def sift(ln, low, high):
    """
    假设此时，ln只有最顶层的节点不符合大根堆的条件。其余节点都符合大根堆的条件
    sift函数进行调整，让整个集合符合大根堆的条件
    :param ln: 需要排序的集合元素
    :param low: 第一个元素
    :param high: 最后一个元素
    :return:
    """
    # 记录顶层节点的值
    temp = ln[low]
    # 初始状态父节点的位置
    i = low
    # 初始状态左子节点的位置
    j = 2 * i + 1
    while j <= high:
        # 必须满足子节点的位置j必须小于集合最后一个元素位置high
        if j + 1 <= high and ln[j + 1] > ln[j]:
            # 如果有右子节点，并且右子节点的值大于左子节点，让j等于右子节点的位置
            j += 1
        if ln[j] > temp:
            # 如果子节点的值大于temp，把子节点的移动到父节点上
            ln[i] = ln[j]
            i = j
            j = 2 * i + 1
        else:
            # 如果子节点不比父节点大，那么说名此时已经符合大根堆的条件，停止循环
            break
    # 将temp的值放到i位置上
    ln[i] = temp


def heap_sort(ln):
    """

    :param ln:
    :return:
    """
    # 1，找最后一个父节点
    # 最后一个节点位置
    n = len(ln) - 1
    # 最后一个节点的父节点位置
    last_f_pos = (n - 1) // 2
    # 2,遍历 建堆
    for i in range(last_f_pos, -1, -1):
        sift(ln, i, n)

    # 3, 此时
    # todo: 完成堆排序练习代码


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # [2,3,1,4, 19] 5
    possible = []
    occur = set()
    for i, n1 in enumerate(nums):
        if i in occur:
            continue
        n2 = target - n1
        print('occur:', occur)
        if n1 != n2:
            if nums.count(n2) == 1 and i != nums.index(n2):
                possible.append([i, nums.index(n2)])
                occur.add(i)
                occur.add(nums.index(n2))
        else:
            if nums.count(n1) == 2:
                print('here')
                print(occur)
                possible.append([i, nums.index(n2, i + 1)])
                occur.add(i)
                occur.add(nums.index(n2, i + 1))

    print(possible)

    if possible:
        return possible[0]
    else:
        return False


def search_matrix(matrix, target):
    """

    :param matrix: r
    :param target:
    :return:
    """
    new_l = []
    for i in matrix:
        new_l.extend(i)
    return target in new_l


class Stack:
    def __init__(self):
        self._data = []

    def pop(self):
        if self._data:
            return self._data.pop()

    def push(self, value):
        self._data.append(value)

    def get_top(self):
        if self._data:
            return self._data[-1]

    def get_count(self):
        return len(self._data)


def parenthesis_matching(str1):
    """
    检查括号是否合法
    eg: '(3+2)[abc]([{sd}sf]ccc)
    :param str1:
    :return:
    """
    s = Stack()
    for c in str1:
        if c in '([{':
            s.push(c)
        elif c in '}])':
            if s.get_count() == 0:
                return False
            o = s.pop()
            if o == '}':
                if c != '{':
                    return False
            elif o == ']':
                if c != '[':
                    return False
            elif o == ')':
                if c != '(':
                    return False
    if s.get_count():
        return False
    else:
        return True


class Queue:
    def __init__(self, size):
        # 设置队列长度
        self.size = size
        self._data = [0 for _ in range(size)]
        # 队列头部指针
        self.front = 0
        # 队列尾部指针
        self.rear = 0

    def push(self, value):
        """
        向队列中添加元素
        :param value:
        :return:
        """
        if not self.is_full():
            # 队列尾部指向的位置向后移动1个位置, 如果长度位置索引超过了队列的size，循环使用前边的位置
            self.rear = (self.rear + 1) % self.size

            self._data[self.rear] = value
        else:
            return '队列已经满了'

    def pop(self):
        """
        弹出front指针指向的元素
        :return:
        """
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self._data[self.front]
        else:
            return '队列是空的'

    def is_empty(self):
        """
        判断队列是否为空
        :return:
        """
        return self.front == self.rear

    def is_full(self):
        """
        判断队列是否满了
        如果满了，不能再向其中添加元素
        :return:
        """
        return (self.rear + 1) % self.size == self.front




if __name__ == '__main__':
    # s1 = 'helloolleh'
    # q = Deque(s1)
    # print(q.judge)
    # l = [11, 5, 8, 3, 2, 10, 1, 12]
    # partition(l, 0, len(l)-1)
    # print(l)
    # quick(l, 0, len(l) - 1)
    # print(l)
    # heap_sort(l)
    # print(l)
    # l = [3, 3]
    # tar = 6
    # print(twoSum(l, tar))
    # search_matrix([[1,2,3], [4,5,6]], 0)
    # str1 = 'hello(){[sdfsdf()]}ab{[gs])}c'
    # print(parenthesis_matching(str1))
    q = Queue(12)
    for i in range(12):
        s = q.push(i)
        print("s:", s)

    for i in range(12):
        s = q.pop()
        print(s)


