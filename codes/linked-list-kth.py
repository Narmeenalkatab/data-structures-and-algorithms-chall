import unittest

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = LinkedListNode(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def kth_from_end(self, k):
        if k < 0 or self.head is None:
            return None

        slow = fast = self.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        return slow.value if slow is not None else None


class LinkedListTests(unittest.TestCase):
    def test_kth_from_end_greater_than_length(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual(linked_list.kth_from_end(4), None)

    def test_kth_from_end_same_as_length(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual(linked_list.kth_from_end(3), 1)

    def test_kth_from_end_negative_integer(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual(linked_list.kth_from_end(-1), None)

    def test_kth_from_end_single_node_list(self):
        linked_list = LinkedList()
        linked_list.append(1)
        self.assertEqual(linked_list.kth_from_end(0), 1)

    def test_kth_from_end_middle_of_list(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)
        linked_list.append(5)
        self.assertEqual(linked_list.kth_from_end(2), 3)

    def test_kth_from_end_happy_path(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(4)
        linked_list.append(5)
        self.assertEqual(linked_list.kth_from_end(3), 2)

if __name__ == '__main__':
    unittest.main()
