class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        a=[True]*n
        a[0]=a[1]=False
        count=0
        for i in range(2,n):
            if a[i]==True:
                count+=1
                for j in range(i*i,n,i):
                    a[j]=False
        return count
#O(nlogn)