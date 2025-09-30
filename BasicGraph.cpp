/*

A graph data structure with basic operations
Adjacency List


STEPS


1 - #include <list>: For using linked lists (for adjacency list)
    - #include <queue>: For BFS algorithm (uses queue data structure)
    - #include <stack>: For DFS algorithm (uses stack data structure)

2 - private:: These members are only accessible within the class
    - int V: Stores the number of vertices/nodes in the graph
    - vector<list<int>> adj: The adjacency list - a vector where each
    element is a list of integers representing neighbors

3 - Graph(int vertices): Constructor that takes number of vertices
    as parameter
    - V = vertices: Assigns the parameter to the class member V
    - adj.resize(V): Resizes the adjacency list vector to have 'V'
    empty lists

4 - void addEdge(int src, int dest, bool directed = false): Method
    to add an edge
    - src: source vertex

    - dest: destination vertex
    - directed = false: default parameter for undirected graph

    - adj[src].push_back(dest): Adds 'dest' to the adjacency list of
    'src'
    - if (!directed): If graph is undirected (default)
    - adj[dest].push_back(src): Also add reverse edge from dest to src

5 - adj[src].remove(dest): Removes 'dest' from src's adjacency list
    - if (!directed): If undirected graph
    - adj[dest].remove(src): Also remove the reverse edge

6 - for (auto it = adj[src].begin(); ...): Iterates through all
    neighbors of src
    - auto it: Automatic type deduction - 'it' becomes a list iterator

    - adj[src].begin(): Iterator pointing to first element in src's list
    - adj[src].end(): Iterator pointing just after last element

    - if (*it == dest): If current neighbor equals destination
    - return true: Edge exists
    - return false: No edge found after checking all neighbors

7 - vector<int> neighbors: Creates empty vector to store results
    - for (int neighbor : adj[vertex]): Range-based for loop through all
    neighbors

    - neighbors.push_back(neighbor): Adds each neighbor to the result
    vector
    - return neighbors: Returns the vector containing all neighbors

8 - Outer loop: for (int i = 0; i < V; i++): Iterates through all
    vertices
    - cout << "Vertex " << i << ": ": Prints vertex number

    - Inner loop: for (int neighbor : adj[i]): Iterates through all neighbors
    of vertex i
    - cout << neighbor << " ": Prints each neighbor
    - cout << endl: New line after each vertex's neighbors

9 - vector<bool> visited(V, false): Tracks visited vertices, all initially
    false
    - queue<int> q: Queue for BFS traversal
    - visited[startVertex] = true: Mark start vertex as visited

    - q.push(startVertex): Add start vertex to queue
    - while (!q.empty()): Continue until queue is empty
    - int current = q.front(): Get front element from queue

    - q.pop(): Remove front element from queue
    - cout << current << " ": Print current vertex
    - Inner loop visits all unvisited neighbors and adds them to queue

10 - stack<int> st: Stack for DFS traversal
    - st.push(startVertex): Push start vertex to stack
    - while (!st.empty()): Continue until stack is empty

    - int current = st.top(): Get top element from stack
    - st.pop(): Remove top element from stack

    - if (!visited[current]): Only process if not visited
    - Push neighbors in reverse order to maintain correct DFS order

11 - getVertexCount(): Simply returns V (number of vertices)
    - getEdgeCount(): Counts all edges in adjacency lists
    - For undirected graphs, divides by 2 (each edge counted twice)

12 - Inside int main() creates graph, adds edges, tests all operations
    - Shows BFS/DFS traversals
    - Demonstrates edge removal


*/

#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <stack>
using namespace std;

class Graph {
    private:
        int V; // Number of vertices
        vector<list<int>> adj; // Adjacency list

    public:
        Graph(int vertices) {
            V = vertices;
            adj.resize(V);
        }

        // 1. Add edge to the graph
        void addEdge(int src, int dest, bool directed = false) {
            adj[src].push_back(dest);

            // If undirected graph, add reverse edge
            if (!directed) {
                adj[dest].push_back(src);
            }
        }

        // 2. Remove edge from the graph
        void removeEdge(int src, int dest, bool directed = false) {
            adj[src].remove(dest);

            if (!directed) {
                adj[dest].remove(src);
            }
        }

        // 3. Check if edge exists
        bool hasEdge(int src, int dest) {
            for (auto it = adj[src].begin(); it != adj[src].end(); it++) {
                if (*it == dest) {
                    return true;
                }
            }
            return false;
        }

        // 4. Get neighbors of a vertex
        vector<int> getNeighbors(int vertex) {
            vector<int> neighbors;
            for (int neighbor : adj[vertex]) {
                neighbors.push_back(neighbor);
            }
            return neighbors;
        }

        // 5. Print the graph
        void printGraph() {
            cout << "Graph (Adjacent List):" << endl;
            for (int i = 0; i < V; i++) {
                cout << "Vertex " << i << ": ";
                for (int neighbor : adj[i]) {
                    cout << neighbor << " ";
                }
                cout << endl;
            }
        }

        // 6. Breadth-First Search (BFS)
        void BFS(int startVertex) {
            vector<bool> visited(V, false);
            queue<int> q;

            cout << "BFS starting from vertex " << startVertex << ": ";

            visited[startVertex] = true;
            q.push(startVertex);

            while (!q.empty()) {
                int current = q.front();
                q.pop();
                cout <<current << " ";

                for (int neighbor : adj[current]) {
                    if (!visited[neighbor]) {
                        visited[neighbor] = true;
                        q.push(neighbor);
                    }
                }
            }
            cout << endl;
        }

        // 7. Depth-First Search (DFS) - Iterative
        void DFS(int startVertex) {
            vector<bool> visited(V, false);
            stack<int> st;

            cout << "DFS starting from vertex " << startVertex << ": ";

            st.push(startVertex);

            while(!st.empty()) {
                int current = st.top();
                st.pop();

                if (!visited[current]) {
                    visited[current] = true;
                    cout << current << " ";

                    // Push neighbors in reverse order for correct DFS
                    vector<int> neighbors = getNeighbors(current);
                    for (auto it = neighbors.rbegin(); it != neighbors.rend(); it++) {
                        if (!visited[*it]) {
                        st.push(*it);
                        }
                    }
                }   
            }
            cout << endl;
        }

        // 8. Get number of vertices
        int getVertexCount() {
            return V;
        }

        // 9. Get number of edges
        int getEdgeCount(bool directed = false) {
            int count = 0;
            for (int i = 0; i < V; i++) {
                count += adj[i].size();
            }
            return directed ? count : count / 2;
        }
};

int main() {

    // Create a graph with 5 vertices
    Graph g(5);

    // Add edges (undirected graph)
    g.addEdge(0, 1);
    g.addEdge(0, 4);
    g.addEdge(1, 2);
    g.addEdge(1, 3);
    g.addEdge(1, 4);
    g.addEdge(2, 3);
    g.addEdge(3, 4);

    // Print the graph
    g.printGraph();

    // Basic operations
    cout << "\nNumber of vertices: " << g.getVertexCount() << endl;
    cout << "Number of edges: " << g.getEdgeCount() << endl;
    cout << "Edge between 1 and 3 exists: " << (g.hasEdge(1, 3) ? "Yes" : "No") << endl;

    // Get neighbors of vertex 1
    vector<int> neighbors = g.getNeighbors(1);
    cout << "Neighbors of vertex 1: ";
    for (int n : neighbors) {
        cout << n << " ";
    }
    cout << endl;

    // graph traversals
    g.BFS(0);
    g.DFS(0);

    // Remove an edge and show changes
    cout << "\nRemoving edge between 1 and 3..." << endl;
    g.removeEdge(1, 3);
    cout << "Edge between 1 and 3 exists: " << (g.hasEdge(1, 3) ? "Yes" : "No") << endl;

    g.printGraph();

    return 0;
}