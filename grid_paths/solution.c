
int uniquePaths(int a, int b) {
    int t, i, j, n;
    double result;
    
    a -= 1;
    b -= 1;
    
    // we shall calculate (A+1)*(A+2)*(A+3) .. *n / factorial(B)
    
    // make sure that A > B
    if (b > a) {
        t = a;
        a = b;
        b = t;
    }
    
    result = 1;
    
    n = a + b;
    for(i = a + 1, j = 2; i <= n; i++) {
        if (j <= b) {
            result = result * (i * 1.0 / j);
            j++;
        }
        else {
            result = result * i;
        }
    }
    
    for(; j <= b; j++) {
        result = result / j;
    }
    
    return (unsigned int)(result + 0.0000000001);
}