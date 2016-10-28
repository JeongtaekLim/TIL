#include <cmath>
#include <stdio.h>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	/* Enter your code here. Read input from STDIN. Print output to STDOUT */
	int target;
	scanf("%d", &target);
	int n;
	scanf("%d", &n);
	vector<int> arr;
	for (int i_n = 0; i_n < n; i_n++) {
		int tmp;
		scanf("%d", &tmp);
		arr.push_back(tmp);
	}
	for (std::vector<int>::iterator i = arr.begin(); i != arr.end(); i++) {
		if (*i == target) {
			printf("%d\n", i - arr.begin());
		}
	}
	return 0;
}
