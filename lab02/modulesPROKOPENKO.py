import random
def quickSort(numbers):
    """
    The function sorts the list in ascending order. Returns an already sorted list.
    
    Parameters
    ----------
    numbers : list.

    Returns
    -------
    list.

    """
    if ( len(numbers) < 2 ):
        return numbers
    else:
        centerNumber = random.choice(numbers)
    smallNumbers = [ number for number in numbers if ( number < centerNumber )]
    largNumbers = [ number for number in numbers if ( number > centerNumber )]
    centerNumbers = [centerNumber] * numbers.count(centerNumber)
    return quickSort(smallNumbers) + centerNumbers + quickSort(largNumbers)

def findElem(elem,list):
    """
    
    The function looks for a given element in the list. If such an element exists, then its index in the list will be returned, and if there is no such element, then None will be returned.
    
    Parameters
    ----------
    elem : int or  float or str .
    list : list.

    Returns
    -------
    int or None.

    """
    if (elem in list):
        return list.index(elem)
    else:
        return None
 

def findListInList(mainList,listForFind):
    """
    The function looks for a list of elements in another list. If such a situation exists, then the initial index of the list will be returned, which should be found in the main list, and if such a situation does not exist, then None will be returned.
    
    Parameters
    ----------
    mainList : list.
    listForFind : list.

    Returns
    -------
    int or None.

    """
    for i in range(len(mainList)):
        tempArray = []
        if len(listForFind) <= len(mainList) - i:
            for j in range(len(listForFind)):
                if listForFind[j] == mainList[i+j]:
                    tempArray.append(listForFind[j])
                else:
                    break               
            if tempArray == listForFind:
                return i    
    return None
    
def findFiveMax(list):
    """
    The function returns the 5 elements with the largest value in the list. If the list contains less than 5 elements, a descending sorted list will be returned.    

    Parameters
    ----------
    list : list.

    Returns
    -------
    list.

    """
    if ( len(list) < 6 ):
        list = quickSort(list)
        list.reverse()
        return list
    else:
        maxList = []
        list2 = []
        list2 = list.copy()
        for i in range(5):
            maxList.append(max(list2))
            list2.remove(max(list2))
        return maxList
    
def findFiveMin(list):
    """
    The function returns the 5 elements with the smallest value in the list. If the list contains less than 5 elements, an ascending sorted list will be returned.

    Parameters
    ----------
    list : list.

    Returns
    -------
    list.

    """
    if ( len(list) < 6 ):
        return quickSort(list)
    else:
        minList = []
        list2 = list.copy()
        for i in range(5):
           minList.append(min(list2))
           list2.remove(min(list2))
        return minList
    
def average(list):
    """
    The function returns the arithmetic mean of all the elements in the list. If the number of elements in the list is less than one, it will be return value of None

    Parameters
    ----------
    list : list.

    Returns
    -------
    float.

    """
    if len(list) > 0:
        return sum(list)/len(list)
    return None

def deleteClone(list):
    """
    The function removes all duplicate elements in the list and leaves only the first element of the same elements from the beginning of the list.

    Parameters
    ----------
    list : list.

    Returns
    -------
    list : list.

    """
    
    list.reverse()
    for i in list:
        object = i
        while(list.count(object) > 1):
            list.remove(object)
    list.reverse()
    return list
            
        






