class Sort_Algorithms(object):
    def __init__(self):
        self.sort_me = [9, 2, 1, 4, 7, 6, 5, 3, 8]

    def __str__(self):
        return str(f"\t[ Sorting Algorithm Demo ]\n" 
            f"Unsorted List:  {self.sort_me}\n"
            f"Bubble Sort:    {self.bubble_sort(self.sort_me)}\tBig-O: O(n^2)\n"
            f"Selection Sort: {self.selection_sort(self.sort_me)}\tBig-O: O(n^2)\n"
            f"Insertion Sort: {self.insertion_sort(self.sort_me)}\tBig-O: O(n^2)\n"
            f"Heap Sort:      {self.heap_sort(self.sort_me)}\tBig-O: O(nlog(n))\n"
            f"Merge Sort:     {self.merge_sort(self.sort_me)}\tBig-O: O(nlog(n))\n"
            f"Quick Sort:     {self.quick_sort(self.sort_me)}\tBig-O: O(n)")

    def bubble_sort(self, nums):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swapped = True
        return nums