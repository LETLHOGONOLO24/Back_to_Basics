/*

Problem: Longest substring with at most k distinct characters.


SIMULATION


string s = "araaci"
k = 2

int windowStart = 0, maxLength = 0;
unoerdered_map<char, int> charFreq;

i = windowEnd

for loop {
	when windowEnd = 0 {
		char rightChar = s[0] = 'a'
		charFreq[rightChar]++; // {'a':1, ...}
	
		while (charFreq.size() > k) { // 1 > 2 -- FALSE
		}
		
		maxLength = max(maxLength, windowEnd - windowStart + 1);
		// maxLength = max(0, 0 - 0 + 1) = 1;
	}
	
	when windowEnd = 1 {
		char rightChar = s[1] = 'r';
		charFreq[rightChar]++; // {'a':1, 'r':1, ...}
		
		while (charFreq.size() > k) { // 2 > 2 -- FALSE
		}
			
		maxLength = max(maxLength, windowEnd - windowStart + 1);
		// maxLength = max(1, 1 - 0 + 1) = 2;
	}
	
	when windowEnd = 2 {
		char rightChar = s[2] = 'a';
		charFreq[rightChar]++; // {'a':2, 'r':1, ...}
		
		while (charFreq.size() > k) { // 2 > 2 -- FALSE
		}
		
		maxLength = max(maxLength, windowEnd - windowStart + 1);
		// maxLength = max(2, 2 - 0 + 1) = 3;
	}
	
	when windowEnd = 3 {
		char rightChar = s[3] = 'a';
		charFreq[rightChar]++; // {'a':3, 'r':1, ...}
		
		while (charFreq.size() > k) { // 2 > 2 -- FALSE
		}
		
		maxLength = max(maxLength, windowEnd - windowStart + 1);
		// maxLength = max(3, 3 - 0 + 1) = 4;
	}
	
	when windowEnd = 4 {
		char rightChar = s[4] = 'c';
		charFreq[rightChar]++; {'a':3, 'r':1, 'c':1, ...}
		
		while (charFreq.size() > k) { // 3 > 2
			char leftChar = s[windowStart] = s[0] = 'a';
			charFreq[leftChar]--; // charFreq['a']-- {'a':2, 'r':1, 'c':1, ...}
			
			if (charFreq[leftChar] == 0) { FALSE
			}
			windowStart++; // 0 -> 1
			
		}
		// The while loop only stops when charFreq.size() <= 2
		// So since we went from araac -> raac (by decrementing charFreq[leftChar], 
		// we still loop
		
		while (charFreq.size() > k) { 3 > 2
			char leftChar = s[windowStart] = s[1] = 'r';
			charFreq[leftChar]--; {'a':2, 'r':0, 'c':1, ...}
			
			if (charFreq[leftChar] == 0) { // 'r' count = 0
				charFreq.erase(leftChar); // {'a':2, 'c':1, ...}
			}
			windowStart++; 1 -> 2
		}
			
		maxLength = max(maxLength, windowEnd - windowStart + 1);
			// maxLength = max(4, 4 - 2 + 1) = 4;
	}
			
	
	when windowEnd = 5 {
		char rightChar = s[5] = 'i';
		charFreq[rightChar]++; // charFreq['i'] {'a':2, 'c':1, 'i':1}
		
		while (charFreq.size() > k) { // 3 > 2
			char leftChar = s[windowStart] = s[2] = 'a';
			charFreq[leftChar]--; // charFreq['a'] {'a':1, 'c':1, 'i':1}
			
			if (charFreq[leftChar] == 0) { // charFreq['a'] != 0
			}
			windowStart++; 2 -> 3
		}
		maxLength = max(maxLength, windowEnd - windowStart + 1);
			// maxLength = max(4, 5 - 3 + 1) = 4;
	}
	
	return maxLength; // maxLength = 4



*/

#include <iostream>
#include <unordered_map>
using namespace std;

int longestSubstringKDistinct(string s, int k) {
    int windowStart = 0, maxLength = 0;
    unordered_map<char, int> charFreq;

    for (int windowEnd = 0; windowEnd < s.size(); windowEnd++) {
        char rightChar = s[windowEnd];
        charFreq[rightChar]++;

        while (charFreq.size() > k) {
            char leftChar = s[windowStart];
            charFreq[leftChar]--;

            if (charFreq[leftChar] == 0) {
                charFreq.erase(leftChar);
            }
            windowStart++;
        }

        maxLength = max(maxLength, windowEnd - windowStart + 1);
    }
    return maxLength;
}

int main() {
    cout << longestSubstringKDistinct("araaci", 2);
    return 0;
}