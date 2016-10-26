#include <cmath>
#include <stdio.h>
#include <vector>
#include <iostream>
#include <algorithm>
#include <deque>
using namespace std;
typedef struct _vertex {
	int num;
	int priority;
}vertex;
typedef struct _edge {
	int u,v;
	int weight;
}edge;
bool compareByPriority(vertex v1, vertex v2) {
	return v1.priority < v2.priority;
}
std::deque<vertex>::iterator getPos(deque<vertex> &q, int v) {
	for (std::deque<vertex>::iterator it = q.begin(); it != q.end(); it++) {
		if ((*it).num == v) {
			return it;
		}
	}
	return q.end();
}
vector<edge> adjlist[3002];
int main() {
	/* Enter your code here. Read input from STDIN. Print output to STDOUT */
	int numOfNodes, numOfEdges;
	scanf("%d %d", &numOfNodes, &numOfEdges);
	for (int i = 0; i < numOfEdges; i++) {
		int u, v, w;
		scanf("%d %d %d", &u, &v, &w);
		edge e1;
		e1.v = v;
		e1.weight = w;
		adjlist[u].push_back(e1);
		edge e2;
		e2.v = u;
		e2.weight = w;
		adjlist[v].push_back(e2);
	}
	int s;
	scanf("%d", &s);

	// prim's mst
	deque<vertex> jq;
	for (int i = 1; i <= numOfNodes; i++) {
		vertex v;
		v.num = i;
		v.priority = std::numeric_limits<int>::max();
		if (i == s) v.priority = 0;
		jq.push_back(v);
	}
	int ans = 0;
	while (jq.size() > 0) {
		std::sort(jq.begin(), jq.end(), compareByPriority);
		vertex cur = jq.front();
		jq.pop_front();
		ans = ans + cur.priority;
		for (std::vector<edge>::iterator it = adjlist[cur.num].begin(); it != adjlist[cur.num].end(); it++) {
			std::deque<vertex>::iterator curPos = getPos(jq, (*it).v);
			if (curPos != jq.end() && it->weight < curPos->priority) {
				curPos->priority = it->weight;
			}
		}
	}
	printf("%d\n", ans);
	return 0;
}
