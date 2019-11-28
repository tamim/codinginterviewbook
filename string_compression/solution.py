input = "abbcccddddeeabbc"
items = []
n = len(input)
frequency = 0
for i in range(n):
    frequency += 1
    if i == n-1 or input[i] != input[i+1]:
        items.append(input[i])
        items.append(str(frequency))
        frequency = 0

print("".join(items))

