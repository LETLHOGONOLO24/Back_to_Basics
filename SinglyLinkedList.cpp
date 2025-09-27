/*

Create a simple singly linked list and print values.


STEPS


1 - Node* next; - Pointer to next node in list
2 - int data; - Integer to store node value

3 - Node(int val) { - Constructor taking integer value
4 - data = val; - Assign parameter to data member

5 - next = nullptr; - Initialize next pointer to null (important!)
6 - ~Node() { - Destructor (called when node is deleted)

7 - cout << "Node with value " << data << " deleted\n"; - Print
    deletion message
8 - Create first node with value 10, head points to it
    Memory: head → [10|null]

9 - Create second node with value 20, link to first node
    Memory: head → [10|&20] → [20|null]
10 - Create third node with value 30, link to second node
    Memory: head → [10|&20] → [20|&30] → [30|null]

11 - Node* temp = head; Create temporary pointer pointing
    to head (for traversal)
12 - while (temp != nullptr) {
        cout << temp->data << " ";
        temp = temp->next;
    }

    Line 25-28: Traverse and print list
    Iteration 1: temp points to node 10, print "10", move to next node
    Iteration 2: temp points to node 20, print "20", move to next node

    Iteration 3: temp points to node 30, print "30", move to next node
    Iteration 4: temp is nullptr, loop exits
    Output: 10 20 30

13 -     delete head->next->next;
        delete head->next;
        delete head;

        Line 30: Delete third node (value 30) → "Node with value 30
        deleted"
        Line 31: Delete second node (value 20) → "Node with value 20
        deleted"
        Line 32: Delete first node (value 10) → "Node with value 10
        deleted"



*/

#include <iostream>
using namespace std;

class Node {
    public:

    int data;
    Node* next;

    Node(int val) {
        data = val;
        next = nullptr;
    }

    ~Node() {
        cout << "Node with value " << data << "deleted\n";
    }
};

int main() {
    Node* head = new Node(10);
    head->next = new Node(20);
    head->next->next = new Node(30);

    Node* temp = head;

    while (temp != nullptr) {
        cout <<temp->data << " ";
        temp = temp->next;
    }

    delete head->next->next;
    delete head->next;
    delete head;

    return 0;
}