class Solution:
    def firstUniqChar(self, s: str) -> int:
        n=len(s)
        for i in range(n):
            found= False
            for j in range(n):
                if i != j and s[i] == s[j]:
                    found= True
                    break
            if not found:
                return i
           
        return -1
        