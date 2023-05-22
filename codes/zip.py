
#creating node and linkedlist classes
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

def zip_lists(list1, list2):
    # Create a new linked list to store the zipped nodes
    zipped_list = LinkedList()

    current1 = list1.head
    current2 = list2.head

    # Iterate through the lists and alternate between the nodes
    while current1 is not None and current2 is not None:
        # Append the node from the first list
        zipped_list.append(current1.value)
        current1 = current1.next

        # Append the node from the second list
        zipped_list.append(current2.value)
        current2 = current2.next

    # If one list is longer than the other, append the remaining nodes
    remaining = current1 if current1 is not None else current2
    while remaining is not None:
        zipped_list.append(remaining.value)
        remaining = remaining.next

    return zipped_list


#strech goal
def merge_sorted_lists(list1, list2):
    if not list1.head:
        return list2.head
    if not list2.head:
        return list1.head

    merged_list = LinkedList()
    current1 = list1.head
    current2 = list2.head
    if current1.value <= current2.value:
        merged_list.head = current1
        current1 = current1.next
    else:
        merged_list.head = current2
        current2 = current2.next

    current = merged_list.head

    while current1 and current2:
        if current1.value <= current2.value:
            current.next = current1
            current1 = current1.next
        else:
            current.next = current2
            current2 = current2.next
        current = current.next

    if current1:
        current.next = current1
    elif current2:
        current.next = current2

    return merged_list






