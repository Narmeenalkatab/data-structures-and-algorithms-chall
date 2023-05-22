from codes.zip import LinkedList, zip_lists,merge_sorted_lists

def test_zip_lists_example_1():
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(2)

    list2 = LinkedList()
    list2.append(5)
    list2.append(9)
    list2.append(4)

    zipped = zip_lists(list1, list2)
    assert linked_list_to_list(zipped) == [1, 5, 3, 9, 2, 4]

def test_zip_lists_example_2():
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)

    list2 = LinkedList()
    list2.append(5)
    list2.append(9)
    list2.append(4)

    zipped = zip_lists(list1, list2)
    assert linked_list_to_list(zipped) == [1, 5, 3, 9, 4]

def test_zip_lists_example_3():
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(2)

    list2 = LinkedList()
    list2.append(5)
    list2.append(9)

    zipped = zip_lists(list1, list2)
    assert linked_list_to_list(zipped) == [1, 5, 3, 9, 2]

def test_zip_lists_additional_1():
    list1 = LinkedList()
    list1.append(1)

    list2 = LinkedList()
    list2.append(2)

    zipped = zip_lists(list1, list2)
    assert linked_list_to_list(zipped) == [1, 2]

def test_zip_lists_additional_2():
    list1 = LinkedList()
    list2 = LinkedList()

    zipped = zip_lists(list1, list2)
    assert linked_list_to_list(zipped) == []

def test_zip_lists_additional_3():
    list1 = LinkedList()
    list1.append(1)

    list2 = LinkedList()
    list2.append(2)
    list2.append(3)

    zipped = zip_lists(list1, list2)
    assert linked_list_to_list(zipped) == [1, 2, 3]

def test_zip_lists_additional_4():
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)

    list2 = LinkedList()

    zipped = zip_lists(list1, list2)
    assert linked_list_to_list(zipped) == [1, 3, 5]

def test_zip_lists_additional_5():
    list1 = LinkedList()

    list2 = LinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)
    list2.append(8)

    zipped = zip_lists(list1, list2)
    assert linked_list_to_list(zipped) == [2, 4, 6, 8]

def linked_list_to_list(linked_list):
    result = []
    current = linked_list.head
    while current:
        result.append(current.value)
        current = current.next
    return result


test_zip_lists_example_1()
test_zip_lists_example_2()
test_zip_lists_example_3()
test_zip_lists_additional_1()
test_zip_lists_additional_2()
test_zip_lists_additional_3()
test_zip_lists_additional_4()
test_zip_lists_additional_5()
print("All tests passed.")

#tests for strech goal, I put them in one function

def test_merge_sorted_lists():
    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)

    list2 = LinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)

    merged = merge_sorted_lists(list1, list2)
    assert linked_list_to_list(merged) == [1, 2, 3, 4, 5, 6]

    list1 = LinkedList()
    list1.append(1)
    list1.append(3)
    list1.append(5)

    list2 = LinkedList()
    list2.append(2)
    list2.append(4)
    list2.append(6)
    list2.append(8)

    merged = merge_sorted_lists(list1, list2)
    assert linked_list_to_list(merged) == [1, 2, 3, 4, 5, 6, 8]

    list1 = LinkedList()
    list1.append(2)
    list1.append(4)
    list1.append(6)

    list2 = LinkedList()
    list2.append(1)
    list2.append(3)
    list2.append(5)

    merged = merge_sorted_lists(list1, list2)
    assert linked_list_to_list(merged) == [1, 2, 3, 4, 5, 6]

    print("All  streach tests passed.")

test_merge_sorted_lists()
