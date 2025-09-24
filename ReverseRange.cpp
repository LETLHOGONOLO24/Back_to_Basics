/*

Problem: Given int arr[] and length n, rotate it right by k positions
(wrap-around). Do it in-place using O(1) extra space.


STEPS


1 - 


*/


#include <iostream>
using namespace std;

void reverse_range(int* a, int*b) {
    while (a < b) {
        swap(*a, *b);
        ++a; --b;
    }
}

void rotate_right(int* arr, int n, int k) {
    if (n <= 1) return;
    k %= n;
    if (k == 0) return;

    reverse_range(arr, arr + n - 1);
    reverse_range(arr, arr + k - 1);
    reverse_range(arr + k, arr + n - 1);
}

int main() {
    int arr[] = {1,2,3,4,5,6,7};
    int n = sizeof(arr)/sizeof(arr[0]);

    rotate_right(arr, n, 3);

    for (int i=0; i < n; ++i) cout<<arr[i]<<" ";
    cout<<"\n";
    return 0;
}