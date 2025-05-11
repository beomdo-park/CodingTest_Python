import sys
string = ""
while True:
    a = sys.stdin.readline().rstrip()
    if not a:
        break
    string+=a+"\n"
print(string)