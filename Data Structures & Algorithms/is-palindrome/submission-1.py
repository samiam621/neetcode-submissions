class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = "".join([char for char in s if char.isalnum()]).lower()
        #base case
        if len(new_s) == 1 or len(new_s) == 0:
            return True
        #recursive case
        elif new_s[0] == new_s[-1]:
            results = True
        else:
            results= False
        results = self.isPalindrome(new_s[1:-1]) & results

        return results