/*

PROBLEM


Given the head of a linked list, determine if the linked list has a
cycle in it.
A cycle occurs if a node’s next pointer points to a previous node in
the list.
You must solve it using O(1) space (no extra data structures).


STEPS




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