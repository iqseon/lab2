def fac(n): #Invite function
    if n == 0:
        return 1
    return fac(n - 1) * n
print(fac(3))