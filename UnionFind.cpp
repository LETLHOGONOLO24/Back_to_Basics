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


-Initialize each node as its own parent
    So each node is its own component initially.
    Example: parent = [0, 1, 2, 3, 4].

-Union operation (unite)
    For each edge (u, v), we connect their sets by changing one’s root
    to point to the other.
    We use union by rank so the smaller tree attaches under the larger
    one — this keeps the structure shallow.

-Find operation (find)
    Uses path compression:
    When we find the root of a node, we make every node on that path
    point directly to the root.
    This speeds up future queries.

-Counting components
    Start with components = n.
    Every successful union (connecting two previously unconnected
    nodes) reduces components by 1.

1 - class UnionFind — defines a disjoint-set data structure. parent
    — parent[i] stores the parent of node i in the disjoint-set forest.
    If parent[i] == i, then i is a root.

2 - rank — rank[i] is an upper-bound heuristic for the depth of the
    tree whose root is i. We use it to attach the smaller tree under
    the larger to keep trees shallow (union by rank).

3 - UnionFind(int n) — constructor to create n singleton sets: {0},
    {1}, ..., {n-1}.
    - parent.resize(n); — allocate space for n parent entries.

    - rank.resize(n, 0); — allocate rank array and initialize all
    ranks to 0.
    - The for loop: parent[i] = i; — set each node’s parent to itself,
    meaning each node is initially the root of its own tree.

    Why rank = 0? When each node is alone, tree height is 0, so rank
    starts at 0. When two trees of equal rank are merged, the rank of
    the new root increases by 1.

4 - find returns the representative (root) of the set that contains x.
    - Base case: if parent[x] == x, x is root → return x.

    - Recursive case: parent[x] != x → call find(parent[x]) to find
    root; then assign parent[x] = find(parent[x]);
    - This both returns the root and compresses the path: after the
    call, x points directly to the root.

    - Effect: repeated find calls become much faster (amortized almost
    constant time).
    - The recursion flattens the tree: nodes along the path from x to
    the root get their parent set to the root.

5 - First, find the roots of x and y (this ensures we operate on tree
    roots).
    - If rootX == rootY, they are already in the same set — nothing to
    do.

    - Otherwise, union by rank:
        - If rank[rootX] > rank[rootY], attach rootY under rootX (parent
        [rootY] = rootX). The taller tree remains root.

        - If rank[rootX] < rank[rootY], attach rootX under rootY.
        - If ranks are equal, attach rootY under rootX and increase
        rank[rootX] by 1 because height increases by 1.

    - Why union by rank? To keep trees shallow, minimizing the cost of
    future find operations.

6 - countComponents computes number of connected components in an undirected
    graph with n nodes and edges.
    - UnionFind uf(n); — instantiate disjoint set for n nodes.

    - int components = n; — initially treat every node as its own component,
    so components = n.
    - Loop over each edge [u, v].

    - rootU = uf.find(u); rootV = uf.find(v); — find current set representatives
    for u and v.
    - If rootU != rootV, the edge connects two previously separate components:

        - uf.unite(u, v); — merge the two sets.
        - components--; — after merging two components become one, so decrement
        count.

    - If rootU == rootV, edge is internal to a component (it doesn’t reduce number
    of components), so do nothing.
    - Note: We call unite(u, v) not unite(rootU, rootV). unite itself calls find,
    so it's fine — redundant finds are acceptable but could be avoided by passing
    roots directly; correctness unaffected.



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