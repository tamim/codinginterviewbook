def binary_search(ara, left, right, target):
    if left > right:
        return -1

    while left <= right:
        mid = (left + right) // 2
        if ara[mid] == target:
            return mid
        if ara[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1 # not found

def two_sum_v1(numbers):
    numbers.sort()
    n = len(numbers)
    for i in range(n-1):
        target = 0 - numbers[i]
        target_index = binary_search(numbers, i+1, n-1, target)
        if target_index > i:
            return numbers[i], numbers[target_index]

def two_sum_v2(numbers):
    found = dict()
    for n in numbers:
        m = 0 - n # or m = n * -1
        try:
            if found[m]:
                return m, n
        except KeyError:
            found[n] = 1
        
def two_sum_v3(numbers):
    numbers.sort()
    n = len(numbers)
    k = n - 1
    for i in range(n-1):
        for j in range(k, -1, -1):
            if numbers[i] + numbers[j] == 0:
                return numbers[i], numbers[j]
            if numbers[i] + numbers[j] < 0:
                k = j
                break

def two_sum_v4(numbers):
    numbers.sort()
    n = len(numbers)
    i, j = 0, n-1
    while i < j:
        if numbers[i] + numbers[j] == 0:
            return numbers[i], numbers[j]
        if numbers[i] + numbers[j] < 0:
            i += 1
        else:
            j -= 1


if __name__ == "__main__":
    numbers = [8, 3, 6, -1, -4, 4, 3, 9, -7]
    print(two_sum_v1(numbers))
    print(two_sum_v2(numbers))
    print(two_sum_v3(numbers))
    print(two_sum_v4(numbers))