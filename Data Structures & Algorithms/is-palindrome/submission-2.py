class Solution:
    def isPalindrome(self, s: str) -> bool:
        #this is much more efficient way to approach using two pointers

        s = s.lower()
        s = "".join(char for char in s if char.isalnum())

        left_pointer = 0
        right_pointer = len(s) - 1

        while left_pointer < right_pointer:
            if s[left_pointer] != s[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1
        return True