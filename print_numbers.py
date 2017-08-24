v1, v2 = map(int, input("Please enter two numbers: ").split())
if v1 >= v2:
    v1, v2 = v2, v1
v1 += 1
while v1 < v2:
    print("The number between v1 and v2 are: " + str(v1))
    v1 += 1