#include <vector>
#include <stdio.h>
using namespace std;
class Solution {
public:
	int countBattleships(vector<vector<char>>& board) {
		int ans = 0;
		for (int i = 0; i < board.size(); i++) {
			for (int j = 0; j < board[i].size(); j++) {
				if (board[i][j] == 'X') {
					if (( j - 1 < 0 || board[i][j - 1] == '.') && (i - 1 < 0 || board[i - 1][j] == '.')&& ( j + 1 > board[i].size() - 1 || board[i][j + 1] == '.' )) {
						ans++;
					}	
					else if (( j - 1 < 0 || board[i][j - 1] == '.') && (i - 1 < 0 || board[i - 1][j] == '.')&&(i + 1 > board.size() - 1 || board[i + 1][j] == '.')){
						ans++;
					}
				}
			}
		}
		return ans;
	}
};
int main() {
	vector<vector<char>> userinput;
	int row, col;
	scanf("%d %d", &row, &col);
	char buf[1024];
	Solution s;
	for (int i = 0; i < row; i++) {
		scanf("%s", buf);
		vector<char> tmp;
		for (int i = 0; i < col; i++) {
			tmp.push_back(buf[i]);
		}
		userinput.push_back(tmp);
	}
	int ans = s.countBattleships(userinput);
	printf("%d\n", ans);
	return 0;
}