class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero, one, two = nums.count(0), nums.count(1), nums.count(2)
        nums[:] = [0] * zero + [1] * one + [2] * two