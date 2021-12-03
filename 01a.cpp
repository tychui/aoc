#include<bits/stdc++.h>
using namespace std;
int main() {
	int a[2000], count = 0;
	for (int i = 0; i < 2000; i++) {
		cin >> a[i];
		if (i >= 1) {
			if (a[i] > a[i-1]) count++;
		}
	}
	cout << count << endl;
	return 0;
}
