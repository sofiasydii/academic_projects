class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            seek = target - num
            if seek in seen:
                return [seen[seek], i]
            seen[num] = i

def main():
    nums = [2, 7, 11, 15]
    target = 9
    solve = Solution()                
    result = solve.twoSum(nums, target) 
    print(result)                        

main()
