class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        f_product = [nums[0]]*len(nums)

        for i in range(1,len(nums)):
            f_product[i] = nums[i]*f_product[i-1]

        b_product = [nums[-1]]*len(nums)
        
        for i in range(len(nums)-2,-1,-1):
            b_product[i] = b_product[i+1]*nums[i]

        ans = [1]*len(nums)
        ans[0] = b_product[1]       
        ans[-1] = f_product[-2]  

        for i in range(1,len(nums)-1):
            ans[i]= f_product[i-1] * b_product[i+1]
        return ans