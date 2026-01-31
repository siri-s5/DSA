class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        a=[]
        for i in letters:
            if ord(i)>ord(target):
                a.append(i)
        if a:
            return a[0]
        return letters[0]