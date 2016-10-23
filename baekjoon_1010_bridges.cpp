#include <stdio.h>
#define NMAX 31
int lookup[NMAX][NMAX];
int comb(int a, int b) {
	if (lookup[a][b] != -1) 
		return lookup[a][b];
	if (lookup[a - 1][b - 1] != -1 && lookup[a - 1][b] != -1) {
		lookup[a][b] = lookup[a - 1][b - 1] + lookup[a - 1][b];
		return lookup[a][b];
	}
	if (a == 0 || b == 0 || a == b) {
		lookup[a][b] = 1;
		return 1;
	}
	return comb(a - 1, b - 1) + comb(a - 1, b);
}
int main() {
	// init lookup table
	for (int i = 0; i < NMAX; i++) {
		for (int j = 0; j < NMAX; j++) {
			lookup[i][j] = -1;
		}
	}
	lookup[0][0] = 1;
	for (int i = 0; i < NMAX; i++) {
		for (int j = 0; j <= i; j++) {
			comb(i, j);
		}
	}
	int testcase;
	scanf("%d", &testcase);
	for (int i_testcase = 0; i_testcase < testcase; i_testcase++) {
		int a, b;
		scanf("%d %d", &a, &b);
		printf("%d\n", lookup[b][a]);
	}
	
	return 0;
}