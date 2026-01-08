class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def center(arr,l,r,m):
            l_sum=float('-inf')
            r_sum=float('-inf')
            temp=0
            for i in range(m,l-1,-1):
                temp+=arr[i]
                l_sum=max(l_sum,temp)
            temp=0
            for i in range(m+1,r+1):
                temp+=arr[i]
                r_sum=max(r_sum,max(temp,arr[i]))
            return l_sum+r_sum
        def recursion_solver(arr,l,r):
            if l==r :
                return arr[l]
            m=(l+r)//2
            left_sum=recursion_solver(arr,l,m)
            right_sum=recursion_solver(arr,m+1,r)
            center_sum=center(arr,l,r,m)
            return max(left_sum,right_sum,center_sum)
        return recursion_solver(nums,0,len(nums)-1)