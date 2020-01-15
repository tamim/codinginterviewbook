#include <stdio.h>

int binary_search(int ara[], int n, int key)
{
    int left, right, mid;
    
    if (n == 0) {
        return 0;
    }   

    left = 0;
    right = n - 1;

    while (left <= right) {
        if (key < ara[left]) {
            return left;
        }
        if (key > ara[right]) {
            return right+1;
        }

        mid = left + (right - left) / 2;
        //printf("l = %d, r = %d, mid = %d, ara[mid] = %d\n", left, right, mid, ara[mid]);
        if (key == ara[mid]) {
            if (mid == left || ara[mid-1] != key) {
                return mid;
            }
            right = mid;
        }
        else if (key < ara[mid]) {
            if (mid > left && key > ara[mid-1]) {
                return mid;
            }
            right = mid - 1;
        }
        else {
            if (mid < right && key < ara[mid+1]) {
                return mid+1;
            }
            left = mid + 1;
        }
    }

    return -1;
}

int main() 
{
    int ara[] = {1, 2, 4, 4, 4, 5, 7, 7};
    int n = 8;
    int key, result;

    int keys[] = {0, 10, 4, 3, 6, 1, 2, 5, 7};
    int i, key_count = 9;

    for (i = 0; i < key_count; i++) {
        key = keys[i];
        result = binary_search(ara, n, key);
        printf("key = %d, pos = %d\n", key, result);
    }
}