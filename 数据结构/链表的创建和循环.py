# -*- coding: UTF-8 -*- 
# created by shenjiannan 2020-10-29 07:59


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def create_link_list_1(lis):
    """
    用头插法创建一个链表，每个节点放到链表的头部
    :param lis:
    :return:
    """
    head = Node(lis[0])
    for i in lis[1:]:
        node = Node(i)
        node.next = head
        head = node
    return head


def create_link_list2(lis):
    """
    创建链表，尾插法
    :param lis:
    :return:
    """
    head = tail = Node(lis[0])
    for i in lis[1:]:
        node = Node(i)
        tail.next = node
        tail = node

    return head


def print_link_list(lin):
    """
    打印一个链表的所有节点
    :param lin:
    :return:
    """
    while lin:
        print(lin.value, end=', ')
        lin = lin.next


if __name__ == '__main__':
    ln = [1, 2, 3, 4, 5]
    link1 = create_link_list_1(ln)
    link2 = create_link_list2(ln)
    print_link_list(link1)
    print('')
    print_link_list(link2)


