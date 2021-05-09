'''
Print out every prime number between 1 and 100.

'''
for n in range(1, 100):
    if n > 1:
        for i in range(2, n):
            if (n%i) == 0:
                break
        else:
            print(n)