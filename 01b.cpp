#include<bits/stdc++.h>
using namespace std;
int main() {
	int measure[2000], count = 0;
	for (int i = 0; i < 2000; i++) cin >> measure[i];
	int a = measure[0]+measure[1]+measure[2];
	for (int i = 1; i < 1999; i++) {
		int b = measure[i]+measure[i+1]+measure[i+2];
		if (b > a) count++;
		a = b;
	}
	cout << count << endl;
	return 0;
}
