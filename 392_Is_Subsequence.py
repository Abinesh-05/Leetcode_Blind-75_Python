class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        slow=0
        
        if s=="":
            return True
        for fast in range(len(t)):
            if s[slow]==t[fast]:
                slow+=1
                
            if slow==len(s):
                return True
        
        return False
