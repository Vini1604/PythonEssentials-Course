c0 = int(input())
steps = 0
while c0 != 1:
    if c0 % 2:
        c0 = 3 * c0 + 1
    else:
        c0//=2
    print(c0)
    steps+=1
print("steps = ", steps)