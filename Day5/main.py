
with open('input.txt') as reader:
    data = reader.readlines()

data = [x.rstrip() for x in data]

def get_row(letters):
    print(letters)

get_row(data[0])