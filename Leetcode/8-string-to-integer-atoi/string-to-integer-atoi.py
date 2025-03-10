class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        result=0
        index=0
        n=len(s)

        #step1 ignore all the leading whitespaces
        while index < n  and s[index] == " ":
            index += 1
        
        #step2 Let's store the sign of the number
        if index < n and (s[index] == "-" or s[index] == "+"):
            if s[index] == "-":
                sign = -1
            index += 1

        #step3 store integer ignore leading zeros and stop when char is found
        while index < n and '0' <= s[index] <='9':
            #append the current digit
            result = result*10 + (ord(s[index]) - ord('0'))

            #handling overflow and underflow
            if result > (2**31 -1):
                if sign == 1:
                    return sign * (2**31 -1 )
                else:
                    return (-2**31)
            index += 1

        return result *sign 