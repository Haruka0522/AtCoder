#include <bits/stdc++.h>
using namespace std;

int main(){
	int n = 0;
	cin >> n;
	vector<pair<int, int>> xy(n);
	for (int i = 0; i < n; i++){
		cin >> xy.at(i).first >> xy.at(i).second;
	}
	for (int i = 0; i < n; i++){
		for (int j = i+1; j < n; j++){
			for (int k = j+1; k < n; k++){
				int x1 = xy.at(i).first;
				int y1 = xy.at(i).second;
				int x2 = xy.at(j).first;
				int y2 = xy.at(j).second;
				int x3 = xy.at(k).first;
				int y3 = xy.at(k).second;
				if ((x2-x1)*(y3-y1) == (x3-x1)*(y2-y1)){
					cout << "Yes" << endl;
					return 0;
				}
			}
		}
	}
	cout << "No" << endl;
	return 0;
}
