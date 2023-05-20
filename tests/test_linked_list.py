import pytest

from codes.linked_list import LinkedList,Node

def test_empty_list():
    ll = LinkedList()
    assert ll.head == None

def test_insert_single_node():
    ll = LinkedList()
    ll.insert(5)
    assert ll.head.value == 5


def test_insert_multiple_nodes():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(10)
    ll.insert(15)
    assert ll.head.value == 15
    assert ll.head.next.value == 10
    assert ll.head.next.next.value == 5

def test_includes():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(10)
    ll.insert(15)
    assert ll.includes(10) == True
    assert ll.includes(20) == False

def test_to_string():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(10)
    ll.insert(15)
    assert ll.to_string() == "{ 15 } -> { 10 } -> { 5 } -> NULL"
