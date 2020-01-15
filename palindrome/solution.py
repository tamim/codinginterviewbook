from timeit import timeit

def is_palindrome1(s):
    return s == s[::-1]
    
def is_palindrome2(s):
    l = len(s)
    indx1 = l // 2 - 1
    indx2 = (l + 1) // 2
    while indx1 >= 0 and indx2 < l:
        if s[indx1] != s[indx2]:
            return False
        indx1, indx2 = indx1 - 1, indx2 + 1

    return True

def run(li, fnc):
    for s in li:
        fnc(s)


if __name__ == "__main__":
    li = ["abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcb"]
    t = timeit(lambda: run(li, is_palindrome1))
    print(t)
    t = timeit(lambda: run(li, is_palindrome2))
    print(t)
