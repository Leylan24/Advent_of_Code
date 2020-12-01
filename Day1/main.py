import itertools as it

with open('input.txt') as reader:
    data = reader.readlines()

data = [int(x.rstrip()) for x in data]

result = []
for i in data:
    for j in data:
        for k in data:
            if(i + j + k == 2020):
                result.append((i,j,k))

print(result)

print(result[0][0]*result[0][1]*result[0][2])
