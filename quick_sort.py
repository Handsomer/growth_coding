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

test_quicksort()