class Solution:
    #step1 removing all the leading zeros         
    def trimLeadingZeroes(self,s):
        #LET'S find position of first '1'
        firstOne=s.find('1')
        if firstOne != -1:
            return s[firstOne:] 
        else:
            return "0"
    def addBinary(self, a: str, b: str) -> str:
        
        #step2 trim leading zeroes
        a = self.trimLeadingZeroes(a)
        b = self.trimLeadingZeroes(b)
        n=len(a)
        m=len(b)

        #step3 swap the strings if a string is smaller than b string
        if n<m:
            a, b = b, a
            n, m = m, n
        
        j= m-1
        carry= 0
        result = []

        #step4 transverse both strings from the end(iterate in reverse order)
        for i in range (n-1,-1,-1):
            #current bit of a
            bit1 =int(a[i])
            bitSum = bit1 + carry
            #if there are remaining bits in b add it to bitsum
            if j>=0:
                #current bit of b
                bit2 =int(b[j])
                bitSum += bit2
                j -= 1

            #calculate result bit and carry
            bit = bitSum%2
            carry = bitSum//2

            result.append(str(bit))

        if carry > 0:
            result.append('1')

        return "".join(result[::-1])