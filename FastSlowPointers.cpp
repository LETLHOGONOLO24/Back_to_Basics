/*

PROBLEM


Given the head of a linked list, determine if the linked list has a
cycle in it.
A cycle occurs if a node’s next pointer points to a previous node in
the list.
You must solve it using O(1) space (no extra data structures).


STEPS


1 - struct ListNode define a singly linked-list node type ListNode:
    - int val; — the data stored in the node.
    - ListNode* next; — pointer to the next node (or NULL/nullptr if
    none).

2 - constructor ListNode(int x) : val(x), next(NULL) {} — initializes
    val with x and sets next to NULL.
3 - declare hasCycle, a function that receives head (pointer to first
    node) and returns true if a cycle exists.

4 - slow — will move one node per loop iteration.
    - fast — will move two nodes per iteration.
5 - the while guard fast != nullptr && fast->next != nullptr ensures:

    - fast exists and fast->next exists so fast->next->next is safe to
    access.
    - If either is nullptr, we've reached the list end → no cycle.

6 - slow = slow->next; — advance slow by 1.
7 - fast = fast->next->next; — advance fast by 2.

8 - if slow == fast (pointer equality), they are pointing to the same
    node in memory ⇒ a cycle exists → return true.
9 - if loop exits, fast hit the end → no cycle → return false.


*/

#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
};

// Function to detect if there's a cycle

bool hasCycle(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;

    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next; // Move slow pointer by 1 step
        fast = fast->next->next; // Move fast pointer by 2 step

        if (slow == fast) { // If they meet, a cycle exists
            return true;
        }
    }

    // Step 3: if fast reaches the end, no cycle
    return false;
}

int main() {
    ListNode* head = new ListNode(3);
    ListNode* second = new ListNode(2);
    ListNode* third = new ListNode(0);
    ListNode* fourth = new ListNode(-4);

    // Connect nodes
    head->next = second;
    second->next = third;
    third->next = fourth;
    fourth->next = second; // Create a cycle

    // test the function
    if (hasCycle(head)) {
        cout << "Cycle detected!" << endl;
    }
    else {
        cout << "No cycle." << endl;
    }

    return 0;
}