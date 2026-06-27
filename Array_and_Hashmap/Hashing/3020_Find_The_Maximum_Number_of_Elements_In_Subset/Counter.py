class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        maximum=0
        hash=Counter(nums)
        for i in hash:
            if i==1:
                total=hash[i] if hash[i]&1 else hash[i]-1
            else:
                total=0
                curr=i
                while curr**2 in hash and hash[curr]>=2:
                    total+=2
                    curr=curr**2
                total+=1
            maximum=max(maximum,total)
        return maximum