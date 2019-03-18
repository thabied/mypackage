def sum_array(array):
    """
    Returns the sum of all integers in an array.

    Args:
        array (array): list of integers

    Returns:
        array: sum of values in the array

    Examples:
        >>>sum_array(np.array([1,2,3,4]))
        10
    """

    if len(array) == 0:  #if the array has only one element, the sum is equal to that element
        return 0
    else:  #grab the first element of the array and repeat for the remaining indexes
        return array[0] + sum_array(array[1:])



def fibonacci(n):
    """
    Return nth term in fibonacci sequence

    Args:
        n (int): nth term in fibonacci sequence to calculate

    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms

    Examples:
        >>> fibonacci(1)
        1
    """

    if n <= 1:  #the second index of the sequence is always 1
        return n
    else:  #repeat the function on the two values before n and add them
        return fibonacci(n-1) + fibonacci(n-2)



def factorial(n):
    """
    Return value for factorial of n

    Args:
        n(int): any positive integer

    Returns:
        integer value equalling the product of every integer before it,
        up until one

    Examples:
        >>> factorial(3)
        6
    """

    if n == 1:  #the factorial of 1 is always 1
        return n
    elif n== 0:
        return 1
    else:  #grab n and repeat the function on the value before n
        return n * factorial(n-1)



def reverse(word):
    """
    Returns the reverse of an entered string

    Args:
        word(str): any single string

    Returns:
        string ordered in the reverse sequence

    Examples:
        >>> reverse(idiot)
        toidi
    """

    if len(word) == 0:  #if no word is entered then the reverse is equal to nothing
        return word
    else:  #grab the first letter and put it last, repeat the function for the remaining indices
        return reverse(word[1:]) + word[0]
