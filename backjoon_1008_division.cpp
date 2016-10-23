// basic concept of division
// information link : http://soen.kr/lecture/ccpp/cpp2/18-1-4.htm
#include <stdio.h>
using namespace std;
int main() {
	double a, b;
	scanf("%lf %lf", &a, &b);
	printf("%.11lf\n", a / b);
	return 0;
}