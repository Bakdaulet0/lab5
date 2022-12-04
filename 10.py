import re
pattern = r"(.+?)([A-Z])"
def to_snake(txt):
    return txt.group(1).lower() + "_" + txt.group(2).lower()
print(re.sub(pattern,to_snake,input()))
