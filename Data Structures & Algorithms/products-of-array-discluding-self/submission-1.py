class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        x=0
        for i in range(len(nums)):
            if nums[i]!=0:
                product=product*nums[i]
            else:
                x=x+1
        y=[]
        for j in range(len(nums)):
            if x==0:
                y.append(product//nums[j])
            elif x==1:
                if nums[j]==0:
                    y.append(product)
                else:
                    y.append(0)
            else:
                y.append(0)

        return y