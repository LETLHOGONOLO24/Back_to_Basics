/*

A graph data structure with basic operations
Adjacency List


STEPS


1 - 



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