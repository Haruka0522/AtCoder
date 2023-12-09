#include <bits/stdc++.h>
#include <algorithm>
using namespace std;

int main(){
	int n = 0;
	cin >> n;
	vector<int> a(n);
	for (int i = 0; i < n; i++){
		cin >> a.at(i);
	}
	int a_max = *max_element(a.begin(), a.end());
	int gcc_max = 0, ans = 0;
	for (int i = 2; i <= a_max; i++){
		//cout << i << endl;
		int gcc_tmp = 0;
		for (int j = 0; j < n; j++){
			if (a.at(j) % i == 0){
				gcc_tmp++;
			}
		}
		if (gcc_max < gcc_tmp){
			gcc_max = gcc_tmp;
			ans = i;
		}
	}
	cout << ans << endl;
	return 0;
}
