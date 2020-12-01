import itertools as it

with open('input.txt') as reader:
    data = reader.readlines()

data =[int(x.rstrip()) for x in data]

#combinations = it.combinations(data,2)
combinations = it.combinations(data,3)

for single in combinations:
    if(single[0]+single[1]+single[2]==2020):
        print(single[0]*single[1]*single[2])
