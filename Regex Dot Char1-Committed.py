
import re

atRegex = re.compile(r'.at')   #just about anything, followed by... "at"
atM0 = atRegex.search('z56ftgy $%^  7tgs7sg  t7gdsty     6ts7gat')
print(atM0.group())
#gat, only the first char before the at + the at

atRegex = re.compile(r'.+at')   #just about anything, followed by... "at"
atM0 = atRegex.search('z56ftgy $%^  7tgs7sg  t7gdsty     6ts7gat')
print(atM0.group())
#z56ftgy $%^  7tgs7sg  t7gdsty     6ts7gat
#the entire string up to and including the at

#################################################################

atRegex = re.compile(r'.at')   #just about anything, followed by... "at"
atM0 = atRegex.findall('z56ftgy $%^  7tgs7sg  t7gdsty     6ts7gat')
print(atM0)
#gat, only the first char before the at + the at


atRegex = re.compile(r'.+at')   #just about anything, followed by... "at"
atM0 = atRegex.findall('z56ftgy $%^  7tgs7sg  t7gdsty     6ts7gat')
print(atM0)
#['z56ftgy $%^  7tgs7sg  t7gdsty     6ts7gat']


#################################################################

atRegex = re.compile(r'.at')   #just about anything, followed by... "at"
atM0 = atRegex.findall('The cat in the hat sat on the flat mat.')
print(atM0)
#['cat', 'hat', 'sat', 'lat', 'mat'], because the dot . means any 1 char before at
#but ONLY 1 character though, before at

atRegex = re.compile(r'.+at')   #just about anything, followed by... "at"
atM0 = atRegex.findall('The cat in the hat sat on the flat mat.')
print(atM0)
#['The cat in the hat sat on the flat mat']  because the dot . means any 1 char
# before "at", but ONLY 1 character though, before at. So FLAT does NOT match here!!!
# .+ looks at ANY wild card char that are longer than 1 chars, which includes SPACES
#and which ends in at at the end of the string.
#displays the whole string because of + and because it ends in "at".

atRegex = re.compile(r'.{1,2}at')   #just about anything, 1 or 2 of those chars
# followed by... "at"
atM0 = atRegex.findall('The cat in the hat sat on the flat mat.')
print(atM0)
#[' cat', ' hat', ' sat', 'flat', ' mat'], this NOW will match with FLAT because 2 chars



