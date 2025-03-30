class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        word= ""
        for ch in s:
            if ch !=" ":
                word += ch
            elif word:
                stack.append(word)
                word=""
        if word:
            stack.append(word)
        return " ".join(stack[::-1])