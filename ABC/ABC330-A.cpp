#include <bits/stdc++.h>
using namespace std;

int main() {
	int n, l = 0;
	cin >> n >> l;
	vector<int> a(n);
	int ans = 0;
	for (int i = 0; i < n; i++){
		cin >> a.at(i);
	}
	for (int j = 0; j < n; j++){
		if (a.at(j) >= l){
			ans++;
		}
	}
	cout << ans << endl;
}
