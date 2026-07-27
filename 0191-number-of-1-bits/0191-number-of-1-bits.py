#class Solution:
#    def hammingWeight(self, n: int) -> int:
#        count=0
#        while n!=0:
#            rem=n%2
#            n//=2
#            if rem==1:
#                count+=1
#        return count
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n:
            count += n & 1
            n >>= 1

        return count