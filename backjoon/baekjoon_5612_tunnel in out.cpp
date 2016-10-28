#include <stdio.h>
int main() {
	int t;
	scanf("%d", &t);
	int incar = 0, carmax = 0;
	scanf("%d", &incar);
	carmax = incar;
	int carinput, caroutput;
	for (int i = 0; i < t; i++) {
		scanf("%d %d", &carinput, &caroutput);
		incar = incar + carinput - caroutput;
		if (incar > carmax) carmax = incar;
		if (incar < 0) {
			carmax = 0;
			break;
		}
	}
	printf("%d\n", carmax);
	return 0;
}