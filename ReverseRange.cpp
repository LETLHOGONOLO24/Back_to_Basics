/*

Problem: Given int arr[] and length n, rotate it right by k positions
(wrap-around). Do it in-place using O(1) extra space.


STEPS


1 - #include <bits/stdc++.h> is the entire C++ Standard Library
    (common in competitive programming)
2 - reverse_range() defines a function that takes two integer
    pointers and reverses elements between them

3 - while (a < b) { continues while start pointer a is before end
    pointer b
4 - swap(*a, *b); swaps the values pointed to by a and b

5 -  ++a; --b; moves start pointer forward and end pointer backward
    This brings pointers closer together for next swap

6 - void rotate_right() is a function to rotate array right by k
    positions. parameters are array pointer, array size, rotation
    amount. We use pointers because we want to modify the original
    array, not work with copies.

    reverse_range(int a, int b) would reverse the first and last element
    not array elements
    The int* is for modifying the first element since arr is like arr[0]

    In C++, arr automatically points to the first element
    Or we can use reverse_range(&arr[0], &arr[0] + n - 1);

7 - if (n <= 1) return; performs early return if array has 0 or 1
    elements (no rotation needed)
8 -  k %= n; ensures k is within array bounds using modulo. Prevents
    unnecessary full rotations (k=7, n=7 → k=0)

9 - if (k == 0) return; early return if no effective rotation needed
10 - reverse_range(arr, arr + n - 1); reverses the entire array. arr
    points to first element, arr + n - 1 points to last element

    arr points to the first element and arr + n - 1 points to the last
    arr + n would be out of bounds

    After rotation: [7,6,5,4,3,2,1]

11 - reverse_range(arr, arr + k - 1); reverses the first k elements.
    After full reversal, first k elements need re-reversal

    After rotation: [5,6,7,4,3,2,1]

12 - reverse_range(arr + k, arr + n - 1); reverses the remaining n-k
    elements. arr + k points to element after the first k elements

    After rotation: [5,6,7,1,2,3,4]


*/


#include <iostream>
using namespace std;

void reverse_range(int* a, int* b) {
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