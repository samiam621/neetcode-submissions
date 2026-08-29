class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # #base case
        if not digits:
            return [1]
        #recursive case
        elif digits[-1] == 9:
            return self.plusOne(digits[:-1]) + [0]
        else:
            digits[-1] += 1
        
        return digits
