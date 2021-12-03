#include<bits/stdc++.h>
using namespace std;
int main() {
	int a[13] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	for (int i = 1; i <= 1000; i++) {
		string s;
		cin >> s;
		for (int j = 0; j <= 11; j++) {
			if (s[j] == '1') a[j]++;
		}
	}
	cout << "Gamma: ";
	for (int i = 0; i <= 11; i++) {
		if (a[i] > 500) cout << "1";
		else cout << "0";
	}
	cout << endl << "Epsilon: ";
	for (int i = 0; i <= 11; i++) {
		if (a[i] < 500) cout << "1";
		else cout << "0";
	}
	return 0;
}