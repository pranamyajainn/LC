class Solution:
    def hIndex(self, citations: List[int]) -> int:
        #step1 sort array in descending order
        citations.sort(reverse=True)
        n=len(citations)
        idx = 0
        #step 2 Keep incrementing idx till citations[idx] > idx
        while idx < n and citations[idx] > idx :
            idx = idx + 1
        return idx 