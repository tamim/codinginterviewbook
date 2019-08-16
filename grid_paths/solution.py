# https://www.interviewbit.com/problems/grid-unique-paths/

from math import factorial

def uniquePaths(A, B):
    A -= 1
    B -= 1
    
    return factorial(A+B) // (factorial(A) * factorial(B))


if __name__ == "__main__":
    A, B = 3, 3
    print(uniquePaths(3, 3))