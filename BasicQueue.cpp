/*

Implement a basic queue (FIFO)


STEPS



1 - int arr[5]; Declares a fixed-size array of 5 integers to store
    queue elements
2 - int front, rear, size; Declares three private member variables:
    front: index of the first element in queue
    rear: index of the last element in queue
    size: current number of elements in queue

3 - Queue() { Constructor that initializes an empty queue:
    front = 0: first element starts at index 0
    rear = -1: indicates no elements in queue
    size = 0: queue is initially empty

4 - void enqueue(int val) { Method to add element to queue, takes
    integer value
5 - if (size == 5) { Checks if queue is full (size equals array capacity),
    throws overflow exception if true

7 - rear = (rear + 1) % 5; Calculates new rear position using modulo
    arithmetic for circular buffer behavior - makes the queue wrap
    around when it reaches the end (wraps back to start)

    If our rear reaches 0 again, the new element will replace the current
    element at arr[0]
8 - arr[rear] = val; Stores the value at the new rear position

9 - if (size == 0) { Checks if queue is empty, throws underflow exception
    if true
10 - int val = arr[front]; Stores the front element value. Temporarily stores
    the front element before removing it

11 - front = (front + 1) % 5; Moves front pointer forward using modulo
    arithmetic. 
    front = (0 + 1) % 5 = 1 since arr[0] wll be logically removed

12 - catch (exception& e) { Catches and displays any exceptions thrown
    by queue operations

    If we remove all the elements in the queue, it will be empty logically
    but the array will still have its old values


*/

#include <iostream>
using namespace std;

class Queue {
    int arr[5];
    int front, rear, size;

    public:
        Queue() {
            front = 0;
            rear = -1;
            size = 0;
        }

        void enqueue(int val) {
            if (size == 5) {
                throw overflow_error("Queue Overflow");
            }
            rear = (rear + 1) % 5;
            arr[rear] = val;
            size++;
        }

        int dequeue() {
            if (size == 0) {
                throw underflow_error("Queue Underflow!");
            }
            int val = arr[front];
            front = (front + 1) % 5;
            size--;
            return val;
        }
};

int main() {
    Queue q;
    try {
        q.enqueue(10);
        q.enqueue(20);
        q.enqueue(30);
        cout << "Dequeued: " << q.dequeue() << endl;
        cout << "Dequeued: " << q.dequeue() << endl;
        cout << "Dequeued: " << q.dequeue() << endl;
    } catch (exception& e) {
        cout << e.what() << endl;
    }
}



