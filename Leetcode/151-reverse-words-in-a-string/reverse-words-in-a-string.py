class Solution:
    def reverseWords(self, s: str) -> str:
        stack = [] 
        word = ""
        for ch in s: 
            #if not space we need to build the word
            if ch!= ' ':
                word += ch
            elif word:
                stack.append(word)
                word= ""
        #pushing last word(without space)
        if word:
            stack.append(word)
        #reverse the stack and rebuild string 
        return " ".join(stack[::-1])
