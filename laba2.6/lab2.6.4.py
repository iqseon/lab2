alph_dict = {'b': 3, 'c': 2, 'a': 4, 'd': 1}
print("Убывание по значениям",sorted(alph_dict.items(), key=lambda item: item[1], reverse=True))