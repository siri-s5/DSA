class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        s=[]
        mini=float('inf')
        for i in range(len(arr)-1):
            mini = min(mini, arr[i+1] - arr[i])
        for j in range(len(arr)-1):
            if abs(arr[j]-arr[j+1])==mini:
                s.append([arr[j],arr[j+1]])
        return s