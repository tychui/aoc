#include<bits/stdc++.h>
using namespace std;
int main() {
	int corrupt = 0;
	for (int i = 1; i <= 98; i++) {
		stack<char> navigation;
		string s;
		cin >> s;
		navigation.push(s[0]);
		for (int j = 1; j < s.length(); j++) {
			if (s[j] == '(' or s[j] == '[' or s[j] == '{' or s[j] == '<') {
				navigation.push(s[j]);
			} else {
				if (s[j] == ')' and navigation.top() == '(') navigation.pop();
				else if (s[j] == ']' and navigation.top() == '[') navigation.pop();
				else if (s[j] == '}' and navigation.top() == '{') navigation.pop();
				else if (s[j] == '>' and navigation.top() == '<') navigation.pop();
				else {
					if (s[j] == ')') corrupt += 3;
					else if (s[j] == ']') corrupt += 57;
					else if (s[j] == '}') corrupt += 1197;
					else if (s[j] == '>') corrupt += 25137;
					break;
				}
			}
		}
	}
	cout << corrupt << endl;
}
