#include <bits/stdc++.h>
using namespace std;

int main(){
	int n, x = 0;
	int s = 0;
	cin >> n >> x;
	int ans = 0;
	for (int i = 0; i < n; i++){
		cin >> s;
		if (s <= x){
			ans += s;
		}
	}
	cout << ans << endl;
}
