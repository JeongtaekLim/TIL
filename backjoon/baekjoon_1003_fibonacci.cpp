#include <stdio.h>
int fres[42][2];
int main() {
	fres[0][0] = 1;
	fres[0][1] = 0;
	fres[1][0] = 0;
	fres[1][1] = 1;
	for (int i = 2; i < 42; i++) {
		for (int j = 0; j < 2; j++) {
			fres[i][j] = fres[i - 1][j] + fres[i - 2][j];
		}
	}
	int testcase;
	scanf("%d", &testcase);
	for (int i_testcase = 0; i_testcase < testcase; i_testcase++) {
		int f;
		scanf("%d", &f);
		printf("%d %d\n", fres[f][0], fres[f][1]);
	}
return 0;
}