

def linear_search(data_list: list[int], key: int) -> tuple[bool, int]:
    '''
    data_list: input list
    key: element to search for

    Return: tuple(True/False, element index)
    '''
    for index,elem in enumerate(data_list):
        if (elem == key):
            return (True,index)
    return (False,-1)



def binary_search(
        data_list: list[int],
        key: int,
        left: int = None,
        right: int = None
) -> tuple[bool, int]:
    '''
    data_list: input list
    key: element to search for
    left: left index of the list
    right: right index of the list


    Return: tuple(True/False, element index)
    '''

    # Setting up left and right index
    if left == None and right == None:
        left = 0
        right = len(data_list) - 1

    while (left <= right):
        mid = left + (right - left)//2;
        elem = data_list[mid]
        if elem == key:
            return (True,mid)
        elif elem > key:    
            right = mid - 1
        elif elem < key:
            left = mid + 1
        
    return (False, -1)




def binary_recursive_search(
        data_list: list[int],
        key: int,
        left: int = None,
        right: int = None
) -> tuple[bool, int]:
    '''
    data_list: input list
    key: element to search for
    left: left index of the list
    right: right index of the list


    Return: tuple(True/False, element index)
    '''

    # Setting up left and right index
    if left == None and right == None:
        left = 0
        right = len(data_list) - 1

    if (left <= right):
        mid = left + (right - left)//2
        elem = data_list[mid]
        if (elem == key):
            return (True,mid)
        elif (elem < key):
            return binary_recursive_search(data_list, key, mid + 1, right)
        elif (elem > key):
            return binary_recursive_search(data_list, key, left, right - 1)
    return (False, -1)

        
    


if __name__ == '__main__':
    print(linear_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
    print(binary_search([1,10,20,30,40,50,90], 10))
    print(binary_recursive_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))