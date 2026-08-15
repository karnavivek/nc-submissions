class Solution:
    def isPalindrome(self, s: str) -> bool:
        #convert the string into a smaller string with only alphanumeric characters
        #remove Non-alphanumeric Characters
        s = s.lower()
        s = "".join(char for char in s if char.isalnum())  
        print(s)

        #two pointers approach, 1st pointer starts from first, 2nd pointer starts from last
        #and then compare them till they coincide
        for i in range(len(s)):
            if s[i]!=s[-i-1]:
                return False
        return True