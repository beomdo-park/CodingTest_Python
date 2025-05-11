user = input()
string= ""
for a in user:
    if a.isupper():
        string+=a.lower()
    else:
        string+=a.upper()
print(string)