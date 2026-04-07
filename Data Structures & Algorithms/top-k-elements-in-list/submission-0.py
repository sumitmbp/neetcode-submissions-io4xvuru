class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]]+=1
            else:
                dict[nums[i]]=1
        x=sorted(dict,key=dict.get,reverse=True)
        y=[]
        for i in range(k):
            y+=[x[i]]
        return y
            

        