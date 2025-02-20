from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def generate(curr: str) -> str:
            # Base case: If the binary string reaches length n
            if len(curr) == n:  
                # Check if it's not in the given set
                if curr not in numsSet:
                    return curr
                return ""  # Return empty if it's already present

            # Try adding '0' first
            add_zero = generate(curr + "0")
            if add_zero:  # If a valid missing string is found, return it immediately
                return add_zero

            # Otherwise, try adding '1'
            return generate(curr + "1")

        # Get the length of binary strings
        n = len(nums[0])  

        # Convert the list to a set for O(1) lookups
        numsSet = set(nums)  

        # Start generating binary strings from an empty string
        return generate("")