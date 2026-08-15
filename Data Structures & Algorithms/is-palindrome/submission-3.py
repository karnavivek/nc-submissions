class Solution:
    def isPalindrome(self, s: str) -> bool:
        #convert the string into a smaller string with only alphanumeric characters
        #remove Non-alphanumeric Characters
        s = s.lower()
        s = "".join(char for char in s if char.isalnum())

        # this is a normal approach, without two pointer & just comparisons
        for i in range(len(s)):
            if s[i]!=s[-i-1]:
                return False
        return True