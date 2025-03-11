class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        n=len(s)
        m=len(t)
        result =[]
        while i<n and j<m:
            if s[i]== t[j]:
                
                result+=s[i]
                i+=1
            j+=1
        if i == len(s): #made it to the end of the string 
            return True
        else:
            return False 