
"""
Given a string s, repeat this operation zero or more times to create the lexicographically smallest string possible.

1. Select two characters that exist in the string, c1 and c2.

2. Replace all occurrences of c1 with c2 and all occurrences of c2with c1.

Note: For two strings xand y of length n, x
 is lexicographically smaller than y
 if the first non-matching character in x
 is less than the character at that position in y.

Input
The first line contains the string s
 (1≤|s|≤105).

Output
The lexicographically smallest string that can be obtained.

Example input
bbcacad

output
aabcbcd

"""


#http://www.thejoboverflow.com/problem/284/
	


text = input()
char_list = sorted(list(set(text)))
char_dict = {}

ctr=0
for c in text:
    if c not in char_dict:
        char_dict[c] = char_list[ctr]
        ctr = ctr+1

res = ""
for c in text:
    res = res + char_dict[c]
    
print(res)
