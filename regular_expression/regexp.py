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

import re

myString = 'Send an email from this@email.com to test@user.com 43 times'

emails = re.findall('\S+@\S+',myString)

print(emails)
