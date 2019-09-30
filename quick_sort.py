#coding:utf-8

def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot_index = 0
        pivot = array[pivot_index]
        less_part = [
            i for i in array[pivot_index + 1 : ] if i <= pivot
        ]
        great_part = [
            i for i in array[pivot_index + 1 : ] if i > pivot
        ]
        return quickSort(less_part) + [pivot] + quickSort(great_part)

def test_quicksort():
    import random
    ll = list(range(10))
    random.shuffle(ll)
    ret_val = quickSort(ll)
    print(ret_val)
    assert ret_val == sorted(ll)

def merge_sorted_list(list_a, list_b):
    length_a, length_b = len(list_a), len(list_b)
    a, b = 0, 0
    ret_list = []
    while a < length_a and b < length_b:
        if list_a[a] <= list_b[b]:
            ret_list.append(list_a[a])
            a += 1
        else:
            ret_list.append(list_b[b])
            b += 1
    if a < length_a:
        ret_list.extend(list_a[a: ])
    if b < length_b:
        ret_list.extend(list_b[b: ])
    return ret_list

def mergeSort(array):
    if len(array) < 2:
        return array
    mid_index = len(array) // 2
    left_list = mergeSort(array[:mid_index])
    right_list = mergeSort(array[mid_index:])
    sorted_list = merge_sorted_list(left_list, right_list)
    return sorted_list

def test_merge():
    import random
    ll = list(range(10))
    random.shuffle(ll)
    ret_list = mergeSort(ll)
    print(ret_list)
    assert ret_list == sorted(ll)

def heapsort_use_heapq(iterable):
    from heapq import heappush, heappop
    items = []
    for value in iterable:
        heappush(items, value)
    return [heappop(items) for i in range(len(items))]

def test_heap():
    import random
    ll = list(range(10))
    random.shuffle(ll)
    ret_list = heapsort_use_heapq(ll)
    print(ret_list)
    assert ret_list == sorted(ll)

# test_heap()
# test_quicksort()
# test_merge()
