#include <bits/stdc++.h>
using namespace std;

int main(){
	int x,y = 0;
	cin >> x >> y;
	if ((0 < y - x) && (y - x < 3)){
		cout << "Yes" << endl;
	} else if ((-4 < y - x) && (y - x < 0)){
		cout << "Yes" << endl;
	} else {
		cout << "No" << endl;
	}
	return 0;
}
