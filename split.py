from tkinter import *
from tkinter import filedialog

final = []
word = ""
word = str(word)

class Rope(object):

    def search_node(self, node, index):

        if node.weight <= index and node.right != None:

            return self.search_node(node.right, index - node.weight)

        elif node.left != None:

            return self.search_node(node.left, index)

        return node, index

    def split_node(self, node, s_index):

        data = node.data
        node1 = Rope(data[:s_index])
        node2 = Rope(data[s_index:])

        return node1, node2

    def helper_split(self, root_node, index):

        t_node, i = self.search_node(root_node, index)

        if t_node.parent == None:

            return self.split_node(t_node,i)

        else:

            if i != 0:

                rope1, rope2 = self.split_node(t_node,i)
                t_node.left = rope1
                t_node.right = rope2
                t_node.weight = len(rope1.data)
                right_node = t_node.right
                t_node.right = None
                t_node.parent.weight -= len(right_node.data)

    def split(self, root, index):

        node, ind = self.search_node(root, index)
        node1 = Rope(node.data[:ind])
        node2 = Rope(node.data[ind:])
        node.data = ""
        node.weight = len(node1.data)
        node.left = node1
        node.right = node2
        node1.parent, node2.parent = node
        split1 = self.helper_split(root, index)
        split2 = self.helper_split(root, 0)
        return split1, split2

