class peak:
    def __init__(self) -> None:
        pass
    
    # an algorithm to find a peak point in an array of distinct points
    # a peak point is defined as point greater than its neighboring point/points
    # parameters: list lst, int i, int j
    # example find_peak(lst, 0, len(lst) - 1)
    # algorithm runs in O(logn)
    def find_peak(self, lst, i, j):
        if i == j:
            return lst[i]
        if abs(i - j) == 1:
            if lst[j] > lst[i]:
                return lst[j]
            else:
                return lst[i]
        mid = abs(j+i) // 2
        if lst[mid] > lst[mid+1] & lst[mid] > lst[mid - 1]:
            return lst[mid]
        if lst[mid + 1] > lst[mid]:
            element = self.find_peak(lst, mid+1, j)
            return element
        else:
            element = self.find_peak(lst, i, mid - 1)
            return element
        
if __name__ == "__main__":
    list1 = [1,5,4,8,10,2,9]
    list2 = [6,9,12,11,3,7]
    list3 = list1+list2
    ls = [2, 1]
    pk = peak()
    print(pk.find_peak(list2, 0, len(list2) - 1))
    
    
    