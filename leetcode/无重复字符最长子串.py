# -*- coding: UTF-8 -*- 
# created by shenjiannan 2020-11-02 22:11


def string_max_substring_length(s):
    """

    :param s:
    :return:
    """
    a = set()
    cur_len = 0
    max_len = 0
    left = 0
    n = len(s)

    for i in range(n):
        # 当前元素
        cur_element = s[i]
        #
        cur_len += 1
        while cur_element in a:
            a.remove(s[left])
            left += 1
            cur_len -= 1
        max_len = cur_len if cur_len > max_len else max_len
        a.add(cur_element)
    return max_len


if __name__ == '__main__':
    m = string_max_substring_length('a')
    print(m)