class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        seen=0
        for i in range(len(nums)):
            seen=target-nums[i]
            if seen in dict:
                return [dict[seen],i]
            else:
                dict[nums[i]]=i


        