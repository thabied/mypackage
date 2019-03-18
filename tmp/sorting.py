def bubble_sort(items):
    """
    The bubble sort algorithm takes in an unsorted list of numbers
    and returns a list in ascending order.

    Args:
        items(list) : list of unordered numbers

    Returns:
        an array of a list of items in ascending order

    Example:
        >>>bubble_sort([5,4,3,2,1])
        [1,2,3,4,5]
    """

    for nums in range(len(items)-1,0,-1):
        for i in range(nums):
            if items[i]>items[i+1]:  #if previous is larger then subsequent, swap them
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp

    return items  #return as an array



def merge(A, B):
    new_list = []
    while len(A) > 0 and len(B) > 0:  #append the smaller value at each index to a new list and remove it from the old list
        if A[0] < B[0]:
            new_list.append(A[0])
            A.pop(0)
        else:
            new_list.append(B[0])
            B.pop(0)

    if len(A) == 0:  #once either list becomes empty, append the other list to new_list
        new_list = new_list + B
    if len(B) == 0:
        new_list = new_list + A

    return new_list


def merge_sort(items):
    """
    The merge sort algorithm takes in an unsorted list of numbers
    and returns a list in ascending order.

    Args:
        items(list) : list of unordered numbers

    Returns:
        an array of a list of items in ascending order

    Example:
        >>>merge_sort([7,3,9,1])
        [1,3,7,9]
    """

    len_i = len(items)
    if len_i == 1:
        return items

    mid_point = int(len_i / 2)  #split the list into 2 at the midpoint
    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])

    return merge(i1, i2)  #merge the 2 lists using the merge function



def quick_sort(items):
    """
    The quick sort algorithm takes in an unsorted list of numbers
    and returns a list in ascending order.

    Args:
        items : list of unordered numbers

    Returns:
        an array of a list of items in ascending order

    Example:
        >>>quick_sort([91,76,13,67,24])
        [13,24,67,76,91]
    """
    len_i = len(items)

    if len_i <= 1:
        return items

    pivot = items[index]
    small = []  #initialize 3 empty lists
    large = []
    dup = []
    for i in items:  #allocate to designated lists based on indices
        if i < pivot:
            small.append(i)
        elif i > pivot:
            large.append(i)
        elif i == pivot:
            dup.append(i)

    small = quick_sort(small)  #update small and large lists by repeating the function
    large = quick_sort(large)

    return small + dup + large
