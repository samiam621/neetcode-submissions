class Solution:

    def isHappy(self, n: int) -> bool:
        return self.helper(n,[])

    def helper(self,n: int,seen=None) -> bool:
        #ex 101 returns False
        #base case
        if n == 1:
            return True
        else:
            #use output of square_digits to recurse helper again
            new_n = self.square_digits(n)
            #add new_n into seen
            if new_n == 1:
                return True
            #check if seen
            elif new_n in seen:
                return False

            seen.append(new_n)
            return self.helper(new_n,seen)
        


        
            
    def square_digits(self,n):
        #ex 101
        #base
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.square_digits(n//10) + (n%10)**2
         


