original_dict = {'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}

print("The original dictionary is : " + str(original_dict))

res = []
for key, val in original_dict.items():
    res.append([key] + val)

# printing result
print("The converted list is : " + str(res))