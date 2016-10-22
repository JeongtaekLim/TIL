#include <vector>
using namespace std;
class Solution {
public:
	
	bool canJump(vector<int>& nums) {
		// case of vector size 1
		if (nums.size() == 1) return true;
		
		int first = 0, second = 0, tmp = 0;
		while (true) {
			tmp = second;
			for (int i = first; i <= second; i++) {
				if (i + nums[i] >= nums.size() - 1) return true;
				if (i + nums[i] > second) {
					second = i + nums[i];
				}
			}
			if (first== second) break;
			first = tmp;
		}
		return false;
	}

};
int main() {
	vector<int> a = { 1,0 };

	Solution s;
	bool result = s.canJump(a);
	result ? printf("true\n") : printf("false\b");
	return 0;
}