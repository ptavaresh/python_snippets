import re

text = open('shakespeare.txt')

for line in text:
    line = line.rstrip()
    if re.search('^[A-Z]{5}$', line):
        print(line)


"""
Regular expressions

^   Start
$   Stop
.   Any character
*   Match one character 0+ times
+   Match one character 1+ times
?   Non-greedy
\s  Whitespace
\S  Non-Whitespace
[abc]   Match one character in the specified set
[^abc]  Match one character not in the specified set
"""
