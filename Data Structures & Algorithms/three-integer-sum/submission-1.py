class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target=0-nums[i]
            left=i+1
            right=len(nums)-1
            while left<right:
                value=nums[left]+nums[right]
                if value>target:
                    right-=1
                elif value<target:
                    left+=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
        return res

        