#!/usr/bin/python3
"""
    a class that defines a node of a singly linked list
"""


class Node:
    """a class(object) that represents a node, note:
        nodes have data and link to the next node"""
    def __init__(self, data, next_node=None):
        """instantiation and initialization of the class attributes"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """private instance data getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """data setter for the getter to receive"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """property setter for next_data, the getter  function"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """property setter for next_data, the setter function"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """a class SinglyLinkedList that defines a singly linked list"""
    def __init__(self):
        """the initialization methoos with no parameter"""
        self.__head = None

    def sorted_insert(self, value):
        """insert the node in a sorted position"""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """a method that print the list"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ("\n".join(values))
