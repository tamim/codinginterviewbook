def calculate_hash(base, s):
    hash_value = 0
    n = len(s)
    for i in range(n):
        hash_value += ord(s[i]) * (base ** (n-1-i))

    return hash_value   

def contains(s, substr):
    # base should be a prime number, 
    # you can use other primes (larger than 256)
    base = 257 

    substr_value = calculate_hash(base, substr)
    
    m = len(substr)

    hash_value = calculate_hash(base, s[:m])
    if substr_value == hash_value:
        if s[:m] == substr: # check to avoid collision
            return True

    power = base ** (m - 1)

    n = len(s)
    for i in range(m, n):
        hash_value -= ord(s[i-m]) * power
        hash_value *= base
        hash_value += ord(s[i])
        
        if substr_value == hash_value:
            if s[i-m+1:i+1] == substr:
                return True

    return False


if __name__ == "__main__":
    s = "this is a test."
    substr = "test"

    if contains(s, substr):
        print(substr, "is present in", s)
    else:
        print(substr, "not found in", s)

    s = "this is a test."
    substr = "thisis"

    if contains(s, substr):
        print(substr, "is present in", s)
    else:
        print(substr, "not found in", s)