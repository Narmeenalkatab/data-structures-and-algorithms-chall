

# def test_append():
#     lst = LinkedList()
#     lst.append(1)
#     assert lst.head.value == 1
#     lst.append(2)
#     assert lst.head.next.value == 2

# def test_insert_before_middle():
#     lst = LinkedList()
#     lst.append(1)
#     lst.append(2)
#     lst.append(4)
#     lst.insert_before(4, 3)
#     assert lst.head.next.next.value == 3

# def test_insert_before_first():
#     lst = LinkedList()
#     lst.append(1)
#     lst.insert_before(1, 0)
#     assert lst.head.value == 0

# def test_insert_after_middle():
#     lst = LinkedList()
#     lst.append(1)
#     lst.append(2)
#     lst.append(4)
#     lst.insert_after(2, 3)
#     assert lst.head.next.next.value == 3

# def test_insert_after_last():
#     lst = LinkedList()
#     lst.append(1)
#     lst.insert_after(1, 2)
#     assert lst.head.next.value == 2
