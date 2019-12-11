def remove_duplicates(nums):
    n = len(nums)
    
    current_index = 1
    for i in range(1, n):
        if nums[i] != nums[i-1]:
            nums[current_index] = nums[i]
            current_index += 1

    return current_index


	
if __name__ == "__main__":
    nums = [1, 1, 1, 2, 3, 3, 4, 4, 4, 5, 6, 6, 7]
    l = remove_duplicates(nums)
    print(nums[:l])
	