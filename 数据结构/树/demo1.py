# -*- coding: UTF-8 -*- 
# created by shenjiannan 2020-12-29 16:57


"""
二叉搜索树🌲
对与任意一个子树🌲,包括树本身，其根节点比左子树都大，比右子树都小
"""


class BiTreeNode:
    """
    二叉树的节点
    """
    def __init__(self, data):
        self.data = data
        self.l_child = None
        self.r_child = None
        self.parent = None


class BST:
    """
    二叉搜索树类
    """
    def __init__(self):
        self.root = None

    def insert(self, node, value):
        if not node:
            node = BiTreeNode(value)
        elif node.data > value:
            node.l_child = self.insert(node.l_child, value)
            node.l_child.parent = node
        elif node.data < value:
            node.r_child = self.insert(node.r_child, value)
            node.r_child.parent = node
        return node

    def insert_no_rec(self, value):
        p = self.root
        if not p:
            self.root = BiTreeNode(value)

        while True:
            if value < p.data:
                if not p.l_child:
                    p.l_child = BiTreeNode(value)
                    p.l_child.parent = p
                    return
                p = p.l_child

            elif value > p.data:
                if not p.r_child:
                    p.r_child = BiTreeNode(value)
                    p.r_child.parent = p
                    return
                p = p.r_child
            else:
                return

    def query(self, value):
        """
        查询节点
        :param value:
        :return:
        """
        p = self.root
        while True:
            if value > p.data:
                if p.r_child:
                    p = p.r_child
                else:
                    return
            elif value < p.data:
                if p.l_child:
                    p = p.l_child
                else:
                    return
            else:
                return p

    def query_with_rec(self, node, value):
        """
        递归查找
        :param node:
        :param value:
        :return:
        """
        if not node:
            return
        elif value < node.data:
            return self.query_with_rec(node.l_child, value)
        elif value > node.data:
            return self.query_with_rec(node.r_child, value)
        else:
            return node

    def pre_order(self, root):
        """
        前序遍历
        :param root:
        :return:
        """
        print(root.data, end=', ')
        if root.l_child:
            self.pre_order(root.l_child)
        if root.r_child:
            self.pre_order(root.r_child)

    def in_order(self, root):
        """
        中序遍历
        :param root:
        :return:
        """
        if root.l_child:
            self.in_order(root.l_child)
        print(root.data, end=', ')
        if root.r_child:
            self.in_order(root.r_child)

    def post_order(self, root):
        """
        后序遍历
        :param root:
        :return:
        """
        if root.l_child:
            self.post_order(root.l_child)
        if root.r_child:
            self.post_order(root.r_child)
        print(root.data, end=', ')


if __name__ == '__main__':
    t = BiTreeNode(100)
    bst = BST()
    bst.root = t
    bst.insert_no_rec(200)
    bst.insert_no_rec(80)
    bst.insert_no_rec(90)
    bst.insert_no_rec(300)
    bst.insert_no_rec(12)
    # bst.pre_order(bst.root)
    # bst.in_order(bst.root)
    d = bst.query_with_rec(bst.root, 12)
    print(d.data)