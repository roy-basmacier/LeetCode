class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def partition(arr, low, high):
            
            pivot = arr[high]
            
            i = low -1
            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i+1], arr[high] = arr[high], arr[i+1]
            return i+1
        
        def quickSort(arr, low, high):
            
            if high<low:
                return
            
            partition_index = partition(arr, low, high)
            
            quickSort(arr, low, partition_index -1)
            quickSort(arr, partition_index +1, high)
        quickSort(nums, 0, len(nums)-1)
        return nums
            
        
        
        