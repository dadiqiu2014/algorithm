# -*- coding: UTF-8 -*- 
# created by shenjiannan 2020-10-27 14:07

"""
给一个二维列表， 表示迷宫， 0 表示通道，1 表示围墙。 给一个算法，求一条走出迷宫的路径
"""

from collections import deque

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]


def func1(m1, n1, m2, n2):
    """
    深度优先
    栈的方法解决
    :param m1 起点横坐标
    :param n1 起点纵坐标
    :param m2 终点横坐标
    :param n2 终点纵坐标
    :return:
    """
    q = deque()
    q.append((m1, n1))
    dirs = [
        lambda x, y: (x + 1, y),
        lambda x, y: (x - 1, y),
        lambda x, y: (x, y + 1),
        lambda x, y: (x, y - 1)
    ]
    while len(q) > 0:
        # print(q)
        # 判断是不是终点
        if q[-1][0] == m2 and q[-1][1] == n2:
            return q
        for d in dirs:
            next_node = d(q[-1][0], q[-1][1])
            if maze[next_node[0]][next_node[1]] == 0:
                q.append(next_node)
                # 标记这个点为已经走过，下次就会再走了
                maze[next_node[0]][next_node[1]] = 2
                break
        else:
            # 如果没有下一个点可走, 出栈
            q.pop()


def func2(m1, n1, m2, n2):
    """
    广度优先
    使用队列
    :param m1:
    :param n1:
    :param m2:
    :param n2:
    :return:
    """
    dirs = [
        lambda x, y: (x + 1, y),
        lambda x, y: (x - 1, y),
        lambda x, y: (x, y + 1),
        lambda x, y: (x, y - 1)
    ]
    # 队列中存储的是所有可能路径的最后一个节点
    # 队列q中存储的数据是包含3个元素的元组，前两个元素是节点位置，最后一个元素是一个列表位置，当前节点是这个位置上的节点寻找过来的
    q = deque()
    # 存储路径祖先节点，类似一个链表
    path = []
    q.append((m1, n1, -1))
    while len(q) > 0:
        # 将最先添加到队列中的位置节点弹出
        current_node = q.popleft()
        path.append(current_node)
        # 判断current_node 是否到达了终点
        if current_node[0] == m2 and current_node[1] == n2:
            # 打印出走过的路径
            real_path = []
            while current_node[2] != -1:
                real_path.append((current_node[0], current_node[1]))
                current_node = path[current_node[2]]
            real_path.append((path[0][0], path[0][1]))
            real_path.reverse()
            return real_path

        # 找当前节点所有可能的下一个位置节点
        for d in dirs:
            next_node = d(current_node[0], current_node[1])
            if maze[next_node[0]][next_node[1]] == 0:
                # 如果这个位置可以走，那么把这个位置加入到队列中
                q.append((next_node[0], next_node[1], len(path) - 1))
                # 将这个位置标记已经走过了
                maze[next_node[0]][next_node[1]] = 2


if __name__ == '__main__':
    # print(func1(1, 1, 6, 1))
    print(func2(1, 1, 6, 1))


