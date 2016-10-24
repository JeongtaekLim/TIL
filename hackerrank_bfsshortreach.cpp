#include <cmath>
#include <cstdio>
#include <vector>
#include <deque>
#include <stdio.h>
#include <algorithm>
#define NMAX 1005
using namespace std;

int main() {
	/* Enter your code here. Read input from STDIN. Print output to STDOUT */
	int testcase;
	scanf("%d", &testcase);
	for (int i_testcase = 0; i_testcase < testcase; i_testcase++) {
		int numV, numE;
		scanf("%d %d", &numV, &numE);
		// edge info
		vector<int> adjlist[NMAX];
		// shortest distance info
		int sdi[NMAX];
		for (int i = 0; i < NMAX;i++) {
			sdi[i] = -1;
		}
		int u, v;
		for (int i_numE = 0; i_numE < numE; i_numE++) {
			scanf("%d %d", &u, &v);
			adjlist[u].push_back(v);
			adjlist[v].push_back(u);
		}
		int s;
		scanf("%d", &s);

		// start bfs
		sdi[s] = 0;
		deque<int> q;
		q.push_back(s);
		while (q.size() > 0) {
			int cur = q.front();
			q.pop_front();
			for (int i = 0; i < adjlist[cur].size(); i++) {
				int n = adjlist[cur][i];
				if (sdi[n] == -1) {
					q.push_back(n);
					sdi[n] = sdi[cur] + 6;
				}
				else if ( sdi[n] > sdi[cur] + 6) {
					sdi[n] = sdi[cur] + 6;
				}
			}
		}
		// print ans
		for (int i_numV = 1; i_numV <= numV; i_numV++) {
			if (i_numV != s) {
				printf("%d ", sdi[i_numV]);
			}
		}
		printf("\n");
	}
	return 0;
}
