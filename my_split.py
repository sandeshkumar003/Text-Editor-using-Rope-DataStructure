from tkinter import *
from tkinter import filedialog

final = []
word = ""
word = str(word)

class Rope(object):

    def __init__(self, value = ""):
        if isinstance(value,str):
            self.left = None
            self.right = None
            self.value = value
            self.weight = len(value)
            #self.parent = None
            #self.current = self
            #self.root = None
            if value == "":
                self.current = self
            else:
                raise TypeError('For time being Only Strings are supported')

    def Indexing(self,index):  
        #node = self.parent
        if self.weight <= index & self.right != None:
            return self.Indexing(self.right,  index - self.weight)
        
        elif self.left != None:
            return self.Indexing(self.left,index)
        
        else:
            return self.value[index]


    def split_node(self, node, s_index):

        value = node.value
        node1 = Rope(value[:s_index])
        node2 = Rope(value[s_index:])

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
                t_node.parent.weight -= len(right_node.value)

    def split(self, root, index):

        node, ind = self.search_node(root, index)
        node1 = Rope(node.value[:ind])
        node2 = Rope(node.value[ind:])
        node.value = ""
        node.weight = len(node1.value)
        node.left = node1
        node.right = node2
        node1.parent, node2.parent = node
        split1 = self.helper_split(root, index)
        split2 = self.helper_split(root, 0)
        return split1, split2   
   
    def concatenation (self, node1, node2):
        new_rope = Rope()
        new_rope.right = node2
        new_rope.left = node1
        new_rope.weight = self.weight(node1)
        #node1.parent = node2.parent = new_rope


    def weight(self,node):          #CONFUSION CHECK Pseodocode
        if node.left == None & node.right == None:
                return len(node.value)
        
        elif node.right == None & node.left != None:
            return self.weight(node.left)

        elif node.right != None & node.left == None:
            return self.weight(node.right)

        else:
            return self.weight(node.right) + self.weight(node.left)
     
    def insertion(self, index_i, s):     # according to Pseodocode
        s1, s2 = self.split(self, index_i)
        final = Rope()

        final.concatenation(s1, s)
        final.concatenation(final, s2)
        return final
    
    def deletion (self, index_i, index_j):
        first,second = self.splits(self,index_j)
        re_first, remove = self.splits (self, index_i)
        final = Rope()
        final.concatenation(re_first,second)
        return final

app = Tk()