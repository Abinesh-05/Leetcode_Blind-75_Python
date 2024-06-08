class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        list=[]
        
        for i in range(max(len(word1),len(word2))):
            if len(word1)<len(word2):
                list.append(word1[i:i+1])
                list.append(word2[i:i+1])
                
            else:
                list.append(word1[i:i+1])
                list.append(word2[i:i+1])
            
        return "".join(list)
