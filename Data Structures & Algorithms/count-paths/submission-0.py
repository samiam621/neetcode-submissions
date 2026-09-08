class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #cache as dict: (i,j) = # of paths
        cache = {}
        return self.paths(m-1,n-1,cache)


    def paths(self,i,j,cache):
        #check if position has routes in cache
        if (i,j) in cache:
            return cache[(i,j)]
        else:
            #base case for edges of grid
            if i == 0 or j == 0:
                return 1
            #recursive
            results = self.paths(i-1,j,cache) + self.paths(i,j-1,cache)
            cache[(i,j)] = results

            return results

        