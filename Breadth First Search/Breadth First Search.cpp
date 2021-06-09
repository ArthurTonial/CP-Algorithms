// https://cp-algorithms.com/graph/breadth-first-search.html

// this code was creatad with the intention of 
// understand how the Breadth First Search works

// Complexity: O(vertices+edges)

#include <bits/stdc++.h>
using namespace std;

#define N ___; // number of nodes
vector<int> adj [N]; // adjacency matrix

queue<int> q;
int used[N]; // indicates for each vertex, if it has been visited or not.
int distance[N]; // array of path lengths
int parents[N]; // array of "parents"

void bfs(int s) { // source vertex

	q.push(s);
	used[s];
	p[s] = -1;

	while (!q.empty()) {
		int u = q.front()
		q.pop();

		for (int i = 0; i < adj[u].size(); i++) {
			int v = adj[u][i];

			if (!used[v]) {
				used[v] = true;
				q.push(v);
				distance[v] = distance[u] + 1;
				parents[v] = u;
			}
		}
	}
}
