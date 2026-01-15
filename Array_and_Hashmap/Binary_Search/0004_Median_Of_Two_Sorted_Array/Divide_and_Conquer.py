class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def find_kth(A:List[int],B:List[int],k:int)->int:
            if not A:return B[k-1]
            if not B:return A[k-1]
            if k == 1: return min(A[0], B[0])
            mid = k // 2
            val_a=A[mid-1] if mid<=len(A) else float('inf')
            val_b=B[mid-1] if mid<=len(B) else float('inf')
            if val_a<val_b:
                return find_kth(A[mid:],B,k-mid)
            else:
                return find_kth(A,B[mid:],k-mid)
        total=len(nums1)+len(nums2)
        if total % 2 == 1:
            return find_kth(nums1,nums2,total//2+1)
        else:
            left=find_kth(nums1,nums2,total//2)
            right=find_kth(nums1,nums2,total//2+1)
            return (left+right)/2.0