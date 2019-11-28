def power_of_2(number):
    if number == "1":
        return True
    if number == "0" or number[0] == "-":
        return False
        
    al = [int(i) for i in number]  

    while True:
        ans = []
        carry = 0
        nonzero = 0
        for n in al:
            d = (n + carry * 10) // 2
            if d:
                nonzero = 1
            if nonzero:
                ans.append(d)
            carry = (n + carry * 10) % 2 
            
        if carry and ans == []:
            return True
        elif carry:
            return False
        al = ans


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        number = input()
        if power_of_2(number):
            print("It's a power of 2")
        else:
            print("Not a power of 2")
