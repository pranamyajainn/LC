class Solution:
    def reverseWords(self, s: str) -> str:
        #split by spaces (automatically removes spaces)
        words = s.split()
        #reverse the word
        words.reverse()
        #join back with single space
        return " ".join(words)