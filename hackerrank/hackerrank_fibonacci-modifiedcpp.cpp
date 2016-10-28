#include <cmath>
#include <stdio.h>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;	
int main() {
	/* Enter your code here. Read input from STDIN. Print output to STDOUT */
	double anstable[22];
	double t1, t2;
	int n;
	scanf("%lf %lf %d", &t1, &t2, &n);
	anstable[1] = t1;
	anstable[2] = t2;
	for (int i_n = 3; i_n <= n; i_n++) {
		anstable[i_n] = anstable[i_n - 2] + (anstable[i_n - 1])*(anstable[i_n - 1]);
	}
	printf("%.0lf\n", anstable[n]);
	return 0;
}
