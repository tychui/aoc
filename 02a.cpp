#include<bits/stdc++.h>
using namespace std;
int main() {
	int hor = 0, ver = 0;
	for (int i = 1; i <= 1000; i++) {
		string s;
		int steps;
		cin >> s >> steps;
		if (s[0] == 'd') ver += steps;
		if (s[0] == 'u') ver -= steps;
		if (s[0] == 'f') hor += steps;
		if (s[0] == 'b') hor -= steps;
	}
	cout << "Horizontal: " << hor << endl;
	cout << "Vertical: " << ver << endl;
	cout << hor*ver << endl;
	return 0;
}
