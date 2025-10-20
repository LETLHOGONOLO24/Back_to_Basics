/*

PROBLEM

You are given an integer n which represents the number of nodes in an
undirected graph (numbered from 0 to n-1) and a list of edges, where
each edge[i] = [u, v] represents a connection between nodes u and v.

Return the number of connected components in the graph.

Example
Input: n = 5, edges = {{0,1}, {1,2}, {3,4}}

Output: 2
Explanation: There are two connected components:
- Component 1: [0, 1, 2]
- Component 2: [3, 4]

Each node starts in its own set (disconnected).
Every time we find an edge (u, v), we union the two sets they belong
to.

After processing all edges, the number of unique sets tells us how
many connected components exist.


STEPS


1 - 



*/

#include <iostream>
#include <vector>
using namespace std;

class UnionFind {
    private:
        vector<int> parent;
        vector<int> rank;

    public:
        UnionFind(int n) {
            parent.resize(n);
            rank.resize(n, 0);

            for (int i = 0; i < n; i++) {

                // Initially, each node is its own parent
                parent[i] = i;
            }
        }

    int find(int x) {

        // Parent Compression Optimization
        if (parent[x] != x)
            parent[x] = find(parent[x]);

        return parent[x];
    }

    void unite(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        // If they have the same root, already connected
        if (rootX == rootY)
            return;

        // Union by rank optimization
        if (rank[rootX] > rank[rootY]) {
            parent[rootY] = rootX;
        }
        else if (rank[rootX] < rank[rootY]) {
            parent[rootX] = rootY;
        }
        else {
            parent[rootY] = rootX;
            rank[rootX] += 1;
        }
    }
};

int countComponents(int n, vector<vector<int>>& edges) {
    UnionFind uf(n);
    int components = n; // Start with all nodes as seperate components

    for (auto& edge : edges) {
        int u = edge[0];
        int v = edge[1];

        int rootU = uf.find(u);
        int rootV = uf.find(v);

        // If they belong to different sets, union them
        if (rootU != rootV) {
            uf.unite(u, v);
            components--; // merging two components into one
        }
    }

    return components;
}

int main() {
    int n = 5;
    vector<vector<int>> edges = {{0,1}, {1,2}, {3,4}};

    cout << "Number of connected components: " << countComponents(n, edges) << endl;

    return 0;
}