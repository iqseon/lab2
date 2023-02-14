"""Instead of int(input()) use map(int, input().split()) to write with a space"""
"""split() - space"""
a, b = [int(i) for i in input('Write two int num use a space, please: ').split()]

print(a, b)

def new_power(a,b):
    return a**b

print('result', new_power(a, b),'end')