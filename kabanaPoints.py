"""	2) Point system = 1, 2, 3, 5, 8,13 (what are the maximum points) """
y = 1

for x in range(1,15):
    y =  1 + y
    mem = y
    mem = mem + y

    print(mem)
