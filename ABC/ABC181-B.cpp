#include <bits/stdc++.h>
using namespace std;

int main(){
	int64_t n = 0;
	cin >> n;
	int64_t ans = 0;
	for (int i = 0; i < n; i++){
		int64_t a, b = 0;
		cin >> a >> b;
		ans += (b+a)*(b-a+1)/2;
	}
	cout << ans << endl;
	return 0;
}
