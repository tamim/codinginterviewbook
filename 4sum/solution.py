
def has_common_elements(p, q):
    if p[1] == q[1] or p[1] == q[2] or p[2] == q[1] or p[2] == q[2]:
        return True
    return False


def four_sum(nums, target):
    pairs = []
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            pairs.append((nums[i]+nums[j], i, j))

    pairs.sort()
    
    n = len(pairs)
    i, j = 0, n-1

    while i < j:
        if pairs[i][0] + pairs[j][0] == target:
            if has_common_elements(pairs[i], pairs[j]):
                continue
            li = [pairs[i][1], pairs[i][2], pairs[j][1], pairs[j][2]]
            li.sort()
            return [nums[x] for x in li]
        elif pairs[i][0] + pairs[j][0] < target:
            i += 1
        else:
            j -= 1

    return []
    
if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(four_sum(nums, target))
    