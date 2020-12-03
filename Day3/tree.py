def check_pos(array, point):
    print(f'LEVEL={point[0]} \t WIDTH={point[1]}')
    if(array[point[0]][point[1]] == '#'):
        return 1
    else:
        return 0

with open('input.txt') as reader:
    data = reader.readlines()

data = [x.rstrip() for x in data]
width = len(data[0])-1
height = len(data)-1
#print(f'width={width} and {data[0][width]}')
level=0
horizontal_pos=0
move=(3,1)
trees=0
position=(level,horizontal_pos)
while(level<height):
    if(horizontal_pos+move[0] <= width):
        horizontal_pos += move[0]
        level+=1
        #print(f'IF: LEVEL={level} \t WIDTH={horizontal_pos}')
    else:
        level+=1
        diff = horizontal_pos+2 - width
        horizontal_pos = diff
        #print(f'ELSE: LEVEL={level} \t WIDTH={horizontal_pos} \t DIFF={diff}') 
    trees += check_pos(data,[level,horizontal_pos])
print(f'{trees}')
