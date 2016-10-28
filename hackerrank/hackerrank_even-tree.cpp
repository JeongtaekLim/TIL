// https://www.cs.cmu.edu/~adamchik/15-121/lectures/Trees/trees.html
#include <cmath>
#include <cstdio>
#include <vector>
#include <stdio.h>
#include <algorithm>
#define NMAX 102
#define INF 999999
using namespace std;

vector<int> edges[NMAX];
int numOfChildInfo[NMAX];
int getNumOfChild(int cur) {
	if (edges[cur].size() == 0)
		return 0;
	int cnt = edges[cur].size();
	for (vector<int>::iterator i = edges[cur].begin(); i != edges[cur].end(); i++) {
		cnt = cnt + getNumOfChild(*i);
	}
	numOfChildInfo[cur] = cnt;
	return cnt;
}
int main() {
	int numV, numE;
	scanf("%d %d", &numV, &numE);
	// edge info input
	for (int i_numE = 0; i_numE < numE; i_numE++) {
		int u, v;
		scanf("%d %d", &u, &v);
		edges[v].push_back(u);
	}
	int cnt = 0;
	while (true) {
		
		for (int i = 0; i < NMAX; i++) {
			numOfChildInfo[i] = -1;
		}
		getNumOfChild(1);
		numOfChildInfo[1] = -1;
		
		int jmin = INF, jidx = 0;
		for (int i = 1; i <= numV; i++) {
			int childCnt = numOfChildInfo[i];
			if (childCnt > 0 && (childCnt + 1) % 2 == 0 && childCnt < jmin) {
				jmin = childCnt;
				jidx = i;
			}
		}

		if (jmin == INF)
			break;

		// eleminate edge info from edges
		for (int i = 1; i <= numV; i++) {
			for (vector<int>::iterator it = edges[i].begin(); it != edges[i].end(); it++) {
				if (*it == jidx) {
					edges[i].erase(it);
					break;
				}
			}
		}
		cnt++;
	}
	printf("%d\n", cnt);
	
	
	return 0;
}

