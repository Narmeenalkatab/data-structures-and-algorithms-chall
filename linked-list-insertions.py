class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        if not self.head:
            raise Exception('List is empty')
        if self.head.value == value:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise Exception('Value not found in list')

    def insert_after(self, target_value, new_value):
        current_node = self.head
        while current_node is not None:
            if current_node.value == target_value:
                new_node = Node(new_value)
                new_node.next = current_node.next
                current_node.next = new_node
                if current_node.next is None:
                    self.tail = new_node
                return
            current_node = current_node.next
        raise ValueError(f"{target_value} not in list")

    def __str__(self):
        if not self.head:
            return "NULL"
        current = self.head
        ll_string = ""
        while current:
            ll_string += f"{{ {current.value} }} -> "
            current = current.next
        ll_string += "NULL"
        return ll_string


def test_append():
    # single value
    ll = LinkedList()
    ll.append(1)
    assert str(ll) == "{ 1 } -> NULL"

    #  multiple values
    ll.append(2)
    ll.append(3)
    assert str(ll) == "{ 1 } -> { 2 } -> { 3 } -> NULL"


def test_insert_before():
    # Test inserting a value before the head of the list
    ll = LinkedList()
    ll.append(1)
    ll.insert_before(1, 2)
    assert str(ll) == "{ 2 } -> { 1 } -> NULL"

    # Test inserting a value before a non-head node
    ll.insert_before(1, 3)
    assert str(ll) == "{ 2 } -> { 3 } -> { 1 } -> NULL"

    # Test inserting a value before a non-existent node
    try:
        ll.insert_before(4, 4)
    except Exception as e:
        assert str(e) == "Value not found in list"


def test_insert_after():
    # Test inserting a value after the head of the list
    ll = LinkedList()
    ll.append(1)
    ll.insert_after(1, 2)
    assert str(ll) == "{ 1 } -> { 2 } -> NULL"

    # Test inserting a value after a non-head node
    ll.append(3)
    ll.insert_after(2, 4)
    assert str(ll) == "{ 1 } -> { 2 } -> { 4 } -> { 3 } -> NULL"

