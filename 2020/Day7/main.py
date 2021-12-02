with open("input.txt") as reader:
    data = reader.readlines()

data = [x.rstrip() for x in data]
for x in data:
    if "shiny" in x:
        print(x)