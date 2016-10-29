#include <cmath>
#include <stdio.h>
#include <queue>
#include <iostream>
#include <algorithm>
#include <limits>
#define NMAX 101
using namespace std;
int main() {
	int testcase;
	scanf("%d", &testcase);
	for (int i_testcase = 0; i_testcase < testcase; i_testcase++) {
		int adjarr[NMAX][NMAX];
		for (int i = 0; i < NMAX; i++) {
			for (int j = 0; j < NMAX; j++) {
				adjarr[i][j] = -1;
				if (i > 0 && j > 0) {
					for (int k = 1; k <= 6; k++) {
						if(i + k <= 100)
							adjarr[i][i + k] = 1;
					}
				}
			}
		}
		int lsarr[NMAX];
		for (int i = 0; i < NMAX; i++) {
			lsarr[i] = -1;
		}
		int ladderN;
		scanf("%d" ,&ladderN);
		for (int i_ladderN = 0; i_ladderN < ladderN; i_ladderN++) {
			int u, v;
			scanf("%d %d", &u, &v);
			//adjarr[u][v] = 1;
			lsarr[u] = v;
		}
		int snakeN;
		scanf("%d", &snakeN);
		for (int i_snakeN = 0; i_snakeN < snakeN; i_snakeN++) {
			int u, v;
			scanf("%d %d", &u, &v);
			//adjarr[u][v] = 1;
			lsarr[u] = v;
		}
		int ans = -1;
		queue<int> jq;
		int disInfo[NMAX];
		for (int i = 0; i < NMAX; i++) {
			disInfo[i] = numeric_limits<int>::max();
		}
		jq.push(1);
		disInfo[1] = 0;
		while (jq.size() > 0) {
			int cur = jq.front();
			jq.pop();
			if (cur == 100) {
				ans = disInfo[cur];
				break;
			}
			for (int i = 1; i < NMAX; i++) {
				if (adjarr[cur][i] == 1 ){
					int next;
					lsarr[i] != -1 ? next = lsarr[i] : next = i;
					if (disInfo[next] > disInfo[cur] + 1) {
						disInfo[next] = disInfo[cur] + 1;
						jq.push(next);
					}
				}
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}
