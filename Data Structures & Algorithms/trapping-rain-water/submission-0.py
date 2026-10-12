class Solution:
    def trap(self, height: list[int]) -> int:
        stored_water = 0
        l_max = height[0]
        r_max = height[-1]
        l,r = 0,len(height)-1

        while l<=r:
            if l_max<=r_max:
                if height[l] <= l_max: 
                    stored_water += (l_max-height[l]) if (l_max-height[l])>0 else 0
                else:
                    l_max=height[l]
                l+=1
                    
            else:
                if height[r]<= r_max:
                    stored_water += (r_max-height[r]) if (r_max-height[r])>0 else 0
                else:
                    r_max=height[r]
                r-=1
        return stored_water