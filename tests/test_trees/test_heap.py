import pytest
from tests import *
from extra.trees._heap import Heap, HeapNode
from extra.trees.heap import MinHeap, MaxHeap



def test_heap_node():
    with pytest.raises(TypeError): HeapNode(None)
    with pytest.raises(TypeError): HeapNode(get_string())
    with pytest.raises(TypeError): HeapNode(get_list())
    val = get_float()
    node = HeapNode(val)
    assert node.get_data() == val
    assert node.get_left() == node.get_right() == None
    assert node.get_children() == []


def test_creating_heap():
    with pytest.raises(TypeError): Heap()
    with pytest.raises(TypeError): Heap.heapify(get_list())


def test_empty_heap(heap = MinHeap()):
    # create it from constructor
    assert len(heap) == 0
    assert heap.is_empty()
    assert str(heap) == "/ \\"
    assert heap.to_list() == []
    assert get_float() not in heap
    assert get_int() not in heap
    get_list() in heap
    get_string() in heap
    with pytest.raises(IndexError): heap.get_min()
    with pytest.raises(IndexError): heap.get_max()
    with pytest.raises(ValueError): heap.insert(None)
    with pytest.raises(TypeError): heap.insert(get_string())
    with pytest.raises(TypeError): heap.insert(get_list())
    #should raise warnings
    with pytest.warns(UserWarning): heap.remove(get_int())
    with pytest.warns(UserWarning): heap.remove(get_float())
    with pytest.warns(UserWarning): heap.remove(get_string())
    with pytest.warns(UserWarning): heap.remove(get_list())


def test_empty_max_heap(heap = MaxHeap()):
    test_empty_heap(heap)
    

def test_empty_heap_using_heapify():
    # test MinHeap
    heap = MinHeap.heapify([])
    test_empty_heap(heap)
    # test MaxHeap
    heap = MaxHeap.heapify([])
    test_empty_heap(heap)


def test_empty_heap_after_clearing():
    # test MaxHeap
    heap = MinHeap()
    heap.insert(10)
    heap.clear()
    test_empty_heap(heap)
    # test MaxHeap
    heap = MaxHeap()
    heap.insert(10)
    heap.clear()
    test_empty_heap(heap)


def test_heap_with_same_value():
    for Heap in [MinHeap, MaxHeap]:
        val = get_float()
        length = get_pos_int()
        lst = [val]*length
        heap = Heap.heapify(lst)
        if Heap == MinHeap:
            assert verify_min_heap(heap._transform()._root)
        elif Heap == MaxHeap:
            assert verify_max_heap(heap._transform()._root)
        assert not heap.is_empty()
        assert heap.to_list() == lst
        assert len(heap) == len(lst)
        assert heap.get_max() == val
        assert heap.get_min() == val
        for node in heap:
            assert node == val
        for _ in range(length):
            heap.remove(val)
        # test_empty_heap(heap)


def test_heapify_of_min_heap_small_example():
    lst = [6, 2, 7, 1]
    heap = MinHeap.heapify(lst)
    assert verify_min_heap(heap._transform()._root)
    assert not heap.is_empty()
    assert len(heap) == len(lst)
    assert heap.get_max() == max(lst)
    assert heap.get_min() == min(lst)
    for num in lst:
        assert num in heap
    assert 19 not in heap
    assert 0 not in heap
    assert get_list() not in heap
    assert get_string() not in heap


def test_heapify_of_min_heap_big_example():
    lst = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17, 90, 100, 102, 190]
    heap = MinHeap.heapify(lst)
    assert len(heap) == len(lst)
    assert verify_min_heap(heap._transform()._root)
    assert heap.get_max() == max(lst)
    assert heap.get_min() == min(lst)
    for node, value in zip(heap, lst):
        assert node == value
    for num in lst:
        assert num in heap
    assert get_list() not in heap
    assert get_string() not in heap


def test_insert_remove_min_heap():
    heap = MinHeap()
    heap.insert(35)
    heap.insert(33)
    heap.insert(42)
    heap.insert(10)
    heap.insert(14)
    heap.insert(19)
    heap.insert(27)
    heap.insert(44)
    heap.insert(26)
    heap.insert(31)
    assert len(heap) == 10
    assert not heap.is_empty()
    assert heap.get_min() == 10
    assert heap.get_max() == 44
    assert verify_min_heap(heap._transform()._root)
    with pytest.warns(UserWarning): heap.remove(0)
    assert len(heap) == 10
    heap.remove(10)
    assert len(heap) == 9
    assert heap.get_min() == 14
    assert heap.get_max() == 44
    assert verify_min_heap(heap._transform()._root)
    heap.remove(44)
    assert len(heap) == 8
    assert heap.get_min() == 14
    assert heap.get_max() == 42
    assert verify_min_heap(heap._transform()._root)


def test_heapify_of_max_heap_small_example():
    lst = [6, 2, 7, 1]
    heap = MaxHeap.heapify(lst)
    assert not heap.is_empty()
    assert verify_max_heap(heap._transform()._root)
    assert len(heap) == len(lst)
    assert heap.get_max() == max(lst)
    assert heap.get_min() == min(lst)
    for node, value in zip(heap,[7, 2, 6, 1]):
        assert node == value
    for num in lst:
        assert num in heap
    assert 19 not in heap
    assert 0 not in heap
    assert get_list() not in heap
    assert get_string() not in heap


def test_heapify_of_max_heap_big_example():
    lst = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17, 90, 100, 102, 190]
    heap = MaxHeap.heapify(lst)
    assert verify_max_heap(heap._transform()._root)
    assert len(heap) == len(lst)
    assert heap.get_max() == max(lst)
    assert heap.get_min() == min(lst)
    for node, value in zip(heap, [190, 15, 102, 8, 13, 17, 100, 1, 5, 4, 9, 3, 10, 6, 90]):
        assert node == value
    for num in lst:
        assert num in heap
    assert get_list() not in heap
    assert get_string() not in heap


def test_insert_remove_max_heap():
    heap = MaxHeap()
    heap.insert(35)
    heap.insert(33)
    heap.insert(42)
    heap.insert(10)
    heap.insert(14)
    heap.insert(19)
    heap.insert(27)
    heap.insert(44)
    heap.insert(26)
    heap.insert(31)
    assert verify_max_heap(heap._transform()._root)
    assert len(heap) == 10
    assert not heap.is_empty()
    assert heap.get_min() == 10
    assert heap.get_max() == 44
    with pytest.warns(UserWarning): heap.remove(0)
    assert len(heap) == 10
    heap.remove(10)
    assert len(heap) == 9
    assert heap.get_min() == 14
    assert heap.get_max() == 44
    assert verify_max_heap(heap._transform()._root)
    heap.remove(44)
    assert len(heap) == 8
    assert heap.get_min() == 14
    assert heap.get_max() == 42
    assert verify_max_heap(heap._transform()._root)


