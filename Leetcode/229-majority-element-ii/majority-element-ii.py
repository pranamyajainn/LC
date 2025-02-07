class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)  # Get the length of the list
        freq = {}      # Dictionary to store frequency of each element

        # Count the frequency of each number in the list
        for num in nums:
            freq[num] = freq.get(num, 0) + 1  # Increase count for num

        result = []  # This list will hold the majority elements

        # Check each number's frequency to see if it appears more than n//3 times
        for num, count in freq.items():
            if count > n // 3:
                result.append(num)

        return result
