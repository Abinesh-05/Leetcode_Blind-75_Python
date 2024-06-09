class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        list1=[]
        list2=[]
        
        for i in range(len(nums)):
            if nums[i]==0:
                list2.append(nums[i])
            else:
                list1.append(nums[i])
        
        list3=list1+list2
                
        for j in range(len(nums)):
            nums[j]=list3[j]
