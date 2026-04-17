class Solution:
    def rev(self,num):
    	reverse=0
    	while num:
    		reverse=(reverse*10)+(num%10)
    		num//=10
    	return reverse
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n=len(nums)
        minimum=n
        hash={}
        for i in range(n):
        	reverse=self.rev(nums[i])
        	if nums[i] in hash:
        		minimum=min(minimum,i-hash[nums[i])
        	hash[reverse]=i
        return -1 if minimum==n else minimum