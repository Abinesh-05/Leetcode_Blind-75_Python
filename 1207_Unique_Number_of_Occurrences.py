class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}

        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]]=1
            else:
                d[arr[i]]+=1
        print(d)

        l=list(d.values())
        count={}

        for j in l:
            if j in count:
                return False
            count[j]=1
        return True 
