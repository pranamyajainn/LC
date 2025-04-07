class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #we use dutch national algorithm (sorting)
        n= len(nums)
        lo = 0 #lo: where the next 0 should be placed
        mid=0 #mid: to transverse the array
        hi = n-1 #hi: position where 2 should be placed
        while mid<=hi:
            if nums[mid] == 0: 
                #swapping
                nums[lo], nums[mid] = nums[mid], nums[lo]
                lo = lo + 1
                mid = mid + 1
            elif nums[mid] == 1:
                mid = mid + 1
            else: 
                nums[mid] , nums[hi] = nums[hi], nums [mid]
                hi = hi -1
        return nums


            