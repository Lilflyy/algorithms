class inversion:
    def __init__(self) -> None:
        pass

    def merge_and_count(self, list1, list2):
        new_list = []
        list1_index, list2_index = 0, 0
        count = 0
        while list1_index < len(list1) and list2_index < len(list2):
            if list1[list1_index] < list2[list2_index]:
                new_list.append(list1[list1_index])
                list1_index += 1
            else:
                new_list.append(list2[list2_index])
                list2_index += 1
                count += len(list1) - list1_index

        new_list.extend(list1[list1_index:])
        new_list.extend(list2[list2_index:])
        return (new_list, count)
    # an algorithm to count inversions within a list
    # takes in a tuple (list, 0)
    # returns a tuple(sorted_list, number of inversions)
    # O(nlogn)
    def count_and_sort(self, tple):
        if len(tple[0]) <= 1:
            return (tple[0], 0)
        lst = tple[0]
        #divide it to two halves
        left = (lst[:len(lst)//2], tple[1])
        right = (lst[len(lst)//2:], tple[1])

        t1 = self.count_and_sort(left)
        t2 = self.count_and_sort(right)
        #merge step
        t3 = self.merge_and_count(t1[0], t2[0])
        #combine
        r = t1[1] + t2[1] + t3[1]
        return (t3[0], r)
    
if __name__ == "__main__":
    list1 = [1,5,4,8,10,2]
    list2 = [6,9,12,11,3,7]
    list3 = list1+list2
    sorter = inversion()
    t = (list3, 0)
    
    ls = sorter.count_and_sort(t)
    print(ls)
    