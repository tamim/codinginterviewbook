
def fourSum(nums, target):
    pairs = []
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            pairs.append((nums[i]+nums[j], i, j))

    print(pairs)        
    pairs.sort()
    print(pairs)
    
    
if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    fourSum(nums, target)
            
    
    