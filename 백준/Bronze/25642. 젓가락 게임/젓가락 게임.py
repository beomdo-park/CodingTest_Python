import sys
yt,yj = map(int,sys.stdin.readline().split())

count = True
while True:
    if yj <5 and yt <5:
        if count == True:
            yj+=yt
            count =False
        elif count == False:
            yt+=yj
            count=True
    else:break
if yj>=5:print('yt')
else:print('yj')