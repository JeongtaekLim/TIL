// Oct, 23, 2016, 1:50am ~ 2:23am
#include <stdio.h>
#include <math.h>
using namespace std;
double getDistance(double x1, double y1, double x2, double y2) {
	double res = 0;
	res = sqrtf((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2));
	return res;
}
int main() {
	int testcase;
	scanf("%d", &testcase);
	for (int i_testcase = 0; i_testcase < testcase; i_testcase++) {
		int circles[51][3];
		int wrapping_circle[51][2];
		int points[2][2];
		// wrapping_circle init
		for (int i = 0; i < 51; i++) {
			for (int j = 0; j < 2; j++) {
				wrapping_circle[i][j] = 0;
			}
		}
		for (int i = 0; i < 2; i++) {
			for (int j = 0; j < 2; j++) {
				scanf("%d", &points[i][j]);
			}
		}
		int num_of_circle;
		scanf("%d", &num_of_circle);
		for (int i = 0; i < num_of_circle; i++) {
			for (int j = 0; j < 3; j++) {
				scanf("%d", &circles[i][j]);
			}
		}
		// for all circles
		for (int i = 0; i < num_of_circle; i++) {
			// for two points
			for (int j = 0; j < 2; j++) {
				double dis = getDistance(circles[i][0], circles[i][1], points[j][0], points[j][1]);
				// if distance is short than r, it is wrapping points
				if (dis < circles[i][2]) {
					wrapping_circle[i][j] = 1;
				}
			}
		}
		int cnt = 0;
		for (int i = 0; i < num_of_circle; i++) {
			if (wrapping_circle[i][0] + wrapping_circle[i][1] == 1) {
				cnt++;
			}
		}
		printf("%d\n", cnt);
	}
	return 0;
}