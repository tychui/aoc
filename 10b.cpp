#include<bits/stdc++.h>
using namespace std;
int main() {
	long long a[98];
	int count = 0;
	for (int i = 1; i <= 98; i++) {
		int corrupt = 0;
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
		if (corrupt == 0 and navigation.empty() == false) {
			long long score = 0;
			while (navigation.empty() == false) {
				score *= 5;
				if (navigation.top() == '(') score += 1;
				if (navigation.top() == '[') score += 2;
				if (navigation.top() == '{') score += 3;
				if (navigation.top() == '<') score += 4;
				navigation.pop();
			}
			a[count] = score;
			count++;
		}
	}
	sort(a, a+count);
	cout << a[(count-1)/2] << endl;
}
