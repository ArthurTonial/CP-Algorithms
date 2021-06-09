// https://cp-algorithms.com/graph/depth-first-search.html

// this code was creatad with the intention of 
// understand how the Depth First Search works

// Complexity: O(vertices+edges)

#include <bits/stdc++.h>
using namespace std;

#define N ___; // number of vertices
vector<int> adj[N]; // graph represented as an adjacency list

vector<bool> visited;

void dfs(int u){

    visited[u] = true;

    for (int i = 0; i < adj[u].size(); i++) {
        int v = adj[u][i];        

        if (!visited[v]) {
            dfs(v);
        }
    }    
}
