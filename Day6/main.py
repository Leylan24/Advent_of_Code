
with open('input.txt') as reader:
    data = reader.readlines()

temp=''
sorted_data = []
for line in data:
    if(line == '\n'):
        sorted_data.append(temp)
        temp=''
    else:
        temp += line
sorted_data.append(temp)
sorted_data = [x.replace('\n','') for x in sorted_data]
def counter(entry):
    count = set()
    for letter in entry:
        count.add(letter)
    return len(count)
counts= 0
for line in sorted_data:
    counts+=counter(line)
print(counts)