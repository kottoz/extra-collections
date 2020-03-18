import pytest
from tests import *
from extra.trees._heap import Heap
from extra.trees.heap import MinHeap, MaxHeap




def test_creating_heap():
    with pytest.raises(TypeError):
        _ = Heap()


def test_heapify_of_min_heap_small_example():
    lst = [6, 2, 7, 1]
    heap = MinHeap.heapify(lst)
    assert heap.to_list() == [1, 2, 7, 6]
    assert len(heap) == len(lst)
    assert heap.get_max() == max(lst)
    assert heap.get_min() == min(lst)
    for node, value in zip(heap, [1, 2, 7, 6]):
        assert node.get_data() == value


