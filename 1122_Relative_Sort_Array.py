class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d={}
        l1=[]
        l2=[]
        for i in arr2:
            d[i]=arr1.count(i)
            
        for i in d:
            l1+=[i,]*d[i]
            
        for j in arr1:
            if j not in arr2:
                l2.append(j)
        
        
        return l1+sorted(l2)
