def maximum_gap(A):
    numbers = []
    for i, num in enumerate(A):
        numbers.append((num, i))
    numbers.sort()
    
    max_gap = 0
    min_number = numbers[0][1]

    for item in numbers:
        num = item[1]
        if num <= min_number:
            min_number = num
        else:
            max_gap = max(max_gap, num - min_number)
    return max_gap



if __name__ == "__main__":
    A = [3, 5, 4, 2]
    print(maximum_gap(A))

    A = [2, 3, 4, 5]
    print(maximum_gap(A))

    A = [5, 4, 3, 2]
    print(maximum_gap(A)) 