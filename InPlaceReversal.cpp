/*

PROBLEM


Given the head of a singly linked list, reverse the list in-place and
return the new head.

That means you are not allowed to use extra data structures like
arrays or stacks — you must modify the pointers directly.

Input: 1 -> 2 -> 3 -> 4 -> 5 -> NULL
Output: 5 -> 4 -> 3 -> 2 -> 1 -> NULL


STEPS


1 - prev keeps track of the previous node (starts as NULL since the
    first node will become the last)
    - current starts at the head node

    - next temporarily stores the next node before we change pointers

2 - while (current != NULL) { We repeat this for every node until
    current becomes NULL.
    - next = current->next; next is the 2nd node or the node next to the
    current

    - current->next = prev; we're saying the pointer that is pointing to
    next is going to point to previous which is null
    - prev = current; we're 
    - current = next; we say current is the next node


*/

#include <iostream>
using namespace std;

// Define the structure for a linked list node
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
};

// Function to reverse a linked list in place
ListNode* reverseList(ListNode* head) {
    ListNode* prev = NULL;
    ListNode* current = head;
    ListNode* next = NULL;

    while (current != NULL) {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    // At the end, prev will point to the new head
    return prev;
}

// Helper function to print the list
void printList(ListNode* head) {
    while (head != NULL) {
        cout << head->val << " ";
        head = head->next;
    }
    cout << endl;
}

int main() {
    ListNode* head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);

    cout << "Original List: ";
    printList(head);

    head = reverseList(head);

    cout << "Reverse List: ";
    printList(head);

    return 0;
}