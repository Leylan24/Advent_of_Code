
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
sorted_data = [x.split('\n') for x in sorted_data]
def counter(entry):
    count = set()
    for letter in entry:
        if letter != '':
            count.add(letter)
    return count
total_count=[]
count_it=0
for line in sorted_data:
    for entry in line:
        if(entry != ''):
            total_count.append(counter(entry))
    print(f'INTERSECTION = {set.intersection(*total_count)} SET = {total_count}')
    count_it+=len(set.intersection(*total_count))
    total_count=[]
    print(f'<-------{count_it}------>')