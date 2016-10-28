#include<stdio.h>
int main() {
	int testcase;
	scanf("%d", &testcase);
	for (int i_testcase = 0; i_testcase < testcase; i_testcase++) {
		int a, b;
		scanf("%d %d", &a, &b);
		int res = 1;
		for (int i = 0; i < b; i++) {
			res = res * a;
			res = res % 10;
		}
		printf("%d\n", res == 0 ? 10 : res);
	}
	return 0;
}