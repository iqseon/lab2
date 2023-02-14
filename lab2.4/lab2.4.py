"""I'm used List Comprehension"""
import random
lnums = list(range(10))
nl = [i + random.random() for i in lnums if not i%2]
print(nl)