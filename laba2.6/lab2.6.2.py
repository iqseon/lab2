number = [(1,1,1), (1,2,3), (-1,-1,7), (-3,-2,8), (0,0,0), (3,-4,-5)]
number.sort(key=lambda x: (x[2]))
print("По третьим элементам из кортежей",number)