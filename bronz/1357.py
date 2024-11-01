def Rev(x):
    for i in range(int(x/2)):
        n = x[i]
        x[i] = x[-i]
        x[-i] = n