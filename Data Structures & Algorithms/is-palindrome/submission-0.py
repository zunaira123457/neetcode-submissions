class Solution:
    def isPalindrome(self, s: str) -> bool:

        L, R = 0, len(s) - 1

        while L < R:
            while L < R and not s[L].isalnum():
                L += 1
            while L < R and not s[R].isalnum():
                R -= 1
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        return True

#The isalnum() method in Python is a built-in string function that returns True if all characters in a string are alphanumeric (letters or numbers) and the string contains at least one character. If the string contains any spaces, symbols, punctuation, or is completely empty, it returns False
