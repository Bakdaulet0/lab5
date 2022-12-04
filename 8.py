import re
print(*re.findall(r'[a-zA-Z][^A-Z]*',input()))