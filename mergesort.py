class mergesort:
    def __init__(self) -> None:
        pass
    def merge(self, list1, list2):
        new_list = []
        list1_index, list2_index = 0, 0

        while list1_index < len(list1) and list2_index < len(list2):
            if list1[list1_index] < list2[list2_index]:
                new_list.append(list1[list1_index])
                list1_index += 1
            else:
                new_list.append(list2[list2_index])
                list2_index += 1

        new_list.extend(list1[list1_index:])
        new_list.extend(list2[list2_index:])
        return new_list
    
    def sort(self, list):
        if (len(list) <= 1):
            return list
        A = list[:len(list)//2]
        B = list[len(list)//2:]
        A = self.sort(A)
        B = self.sort(B)
        new_list = self.merge(A, B)
        return new_list
        
        
    
    
if __name__ == "__main__":
    list1 = [1, 5, 6]
    list2 = [2, 4, 9, 10, 15]
    list3 = [5, 6, 3, 2,9,10, 19]
    sorter = mergesort()
    ls = sorter.sort(list3)
    print(ls)
        

