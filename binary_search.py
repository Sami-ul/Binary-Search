import random


def binary_search(search_list, item):
    """
    Finds the middle of the list,
    checks where that number is relative to item,
    and then splits on the side where item is supposed
    to be and repeats this process until item is the
    middle index.

    List must be sorted
    O log(n) time complexity    
    """
    start_index = 0
    end_index = len(search_list) - 1
    while True:
        middle_index = (start_index + end_index)//2
        if search_list[middle_index] == item:
            return middle_index
        elif search_list[middle_index] > item:
            end_index = middle_index - 1
        elif search_list[middle_index] < item:
            start_index = middle_index + 1

# Everything above is the entire binary search algorithm, everything below this is just creation of a random sorted input for the function.


def list_filler(fill_list, fill_cap):
    count = 0
    while count < fill_cap:
        fill_list.append(random.randint(0, 1000))
        count += 1
    return fill_list


cap = 10
exec_list = []
exec_list = list_filler(exec_list, cap)
exec_list.sort()
search_int = exec_list[random.randint(0, cap - 1)]
print(f"Index of {search_int} in {exec_list}: ",
      binary_search(exec_list, search_int))
