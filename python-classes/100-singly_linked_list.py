#!/usr/bin/python3
"""defines the Data class and SinglyLinkedList class"""


class Node:
    """defines a data object with data and next_node property"""
    def __init__(self, data, next_node=None):
        """Instatiate a Node object
        Args:
            data (int)
            next_node (Node, optional)
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get the __data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets the __data attribute
        Args:
            value (int)
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """gets the __next_node property"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the __next_node property"""
        if type(value) != Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ defines a singly linked list"""
    def __init__(self):
        """instantiate the singlylinkedlist"""
        self.__head = None

    def __str__(self):
        """return the linked list string"""
        print_list = ""
        current = self.__head
        while current:
            if current.next_node is not None:
                print_list += f"{current.data}\n"
            else:
                print_list += f"{current.data}"
            current = current.next_node
        return print_list

    def sorted_insert(self, value):
        """insert a new node"""
        node = Node(value)
        if self.__head is None:
            self.__head = node
        else:
            print("I got here", node.data, self.__head.data)
            if node.data < self.__head.data:
                print("I got here", node.data, self.__head.data)
                node.next_node = self.__head
                self.__head = node
            elif self.__head.next_node is None:
                self.__head.next_node = node
            elif node.data == self.__head.data:
                node.next_node = self.__head.next_node
                self.__head.next_node = node
            else:
                current = self.__head
                while current:
                    if current.next_node is None:
                        current.next_node = node
                        break
                    elif current.next_node.data < node.data:
                        current = current.next_node
                    else:
                        node.next_node = current.next_node
                        current.next_node = node
                        break
