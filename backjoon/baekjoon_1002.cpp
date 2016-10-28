#include <stdio.h>
#include <math.h>
using namespace std;
double getdis(double x1, double y1, double x2, double y2) {
	double res = sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2));
	return res;
}
int main() {
	int testcase;
	scanf("%d", &testcase);
	for (int i_testcase = 0; i_testcase < testcase; i_testcase++) {
		int cnt = 0;
		double x1, y1, r1, x2, y2, r2;
		scanf("%lf %lf %lf %lf %lf %lf", &x1, &y1, &r1, &x2, &y2, &r2);
		double dis = getdis(x1, y1, x2, y2);
		// different two point
		if (!(x1 == x2 && y1 == y2)) {
			// outer meet
			if (dis > r1 && dis > r2) {
				if (dis > r1 + r2) {
					cnt = 0;
				}
				else if (dis == r1 + r2) {
					cnt = 1;
				}
				else if (dis < r1 + r2) {
					cnt = 2;
				}
			}
			// inner meet
			else {
				if (dis < fabs(double(r1) - double(r2))){
					cnt = 0;
				}
				else if (dis == fabs(double(r1) - double(r2))){
					cnt = 1;
				}
				else if (dis  > fabs(double(r1) - double(r2))){
					cnt = 2;
				}
			}
			
		}
		// same point
		else {
			if (r1 == r2) {
				cnt = -1;
			}
			else {
				cnt = 0;
			}
		}
		printf("%d\n", cnt);
	}
	return 0;
}