data = {"A":4.0,
        "B":3.0,
        "C":2.0,
        "D":1.0,
        "F":0}
user= input()
dgree = user[0]

if dgree=="F":
    print(0.0)
else:
    if user[1] == "+":
        pm = 0.3
    elif user[1] == "-":
        pm = -0.3
    else:pm=0
    print(data[dgree]+pm)