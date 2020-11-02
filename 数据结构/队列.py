# -*- coding: UTF-8 -*- 
# created by shenjiannan 2020-10-26 13:22


class Queue:
    """
    这个队列比直接用列表实现的队列效率要高
    因为直接使用列表的append和pop方法实现的队列，添加活着弹出元素的时间复杂度为O(n)
    这个使用循环队列的思想，添加或者弹出的操作时间复杂度为O(1)
    """
    def __init__(self, size):
        # 设置队列固定长度
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
    q = Queue(10)
