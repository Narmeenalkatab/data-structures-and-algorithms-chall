
#node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

#linkedlist
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        if value is None:
            return "Error: Cannot insert a node with a None value"
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def includes(self, value):
        """Indicates whether that value exists as a Node’s value somewhere within the list."""
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def to_string(self):
        """Returns a string representing all the values in the Linked List, formatted as: { a } -> { b } -> { c } -> NULL"""
        current_node = self.head
        linked_list_string = ""
        while current_node:
            linked_list_string += f"{str(current_node.value)} -> "
            current_node = current_node.next
        linked_list_string += "NULL"
        return linked_list_string
