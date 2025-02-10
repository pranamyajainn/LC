from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Rotates the array to the right by k steps.
        """
        n = len(nums)  # Get the length of the array
        k = k % n  # Handle cases where k > n (rotate only within bounds)

        temp = [0] * n  # Create a temporary array of the same size as nums

        # Copy the last k elements to the beginning of temp
        for i in range(k):
            temp[i] = nums[n - k + i]  

        # Copy the first (n-k) elements to the remaining positions in temp
        for i in range(k, n):
            temp[i] = nums[i - k]  

        # Copy elements from temp back to nums to modify in-place
        for i in range(n):
            nums[i] = temp[i]  