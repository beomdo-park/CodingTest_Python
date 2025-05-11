import sys
while True:
    dosi = sys.stdin.readline().rstrip()
    if dosi=='0':
        break
    
    if dosi == dosi[::-1]:
        print('yes')

    else:
        print('no')