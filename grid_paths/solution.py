# https://www.interviewbit.com/problems/grid-unique-paths/

def uniquePaths(A, B):
    A -= 1
    B -= 1
    
    def factorial(n):
        fact = 1
        
        for i in range(2, n+1):
            fact *= i
            
        return fact
        
    return factorial(A+B) // (factorial(A) * factorial(B))


if __name__ == "__main__":
    A, B = 3, 3
    print(uniquePaths(3, 3))