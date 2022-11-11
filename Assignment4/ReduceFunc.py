from functools import reduce

a = [1,2,3,4,5]

result = reduce(lambda n,m: n*m,a)

print(result)
print(type(result))
