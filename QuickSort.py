
class SortingAlgo:
    def __init__(self, alist):
        print("Unsorted Array: \n{}".format(alist))
        self.alist = alist

    def quicksort(self, start, end):
        # print("start: {} end: {}".format(start, end))
        # import pdb
        # pdb.set_trace()
        if start < end:
            p_index = self.partition(start=start, end=end)
            # print("p_index: {}".format(p_index))
            self.quicksort(start, p_index - 1)
            self.quicksort(p_index + 1, end)

    def partition(self, start, end):
        pivot = self.alist[end]
        p_index = start
        # print("pivot={} ".format(pivot))
        for i in range(start, end):
            # print("i={} pivot={} p_index={}".format(i,pivot,p_index))
            if self.alist[i] <= pivot:
                self.alist[p_index], self.alist[i] = self.alist[i], self.alist[p_index]
                p_index += 1
        self.alist[p_index], self.alist[end] = self.alist[end], self.alist[p_index]
        # print("swapped Array: \n{}".format(self.alist))
        return p_index

    def display(self):
        print("Sorted Array: \n{}".format(self.alist))


if __name__ == "__main__":
    arr = [8,3,6,1,9,4,5,2,7,0]
    quickSortObj = SortingAlgo(arr)
    start = 0
    end = len(arr) - 1
    quickSortObj.quicksort(start=start, end=end)
    quickSortObj.display()
