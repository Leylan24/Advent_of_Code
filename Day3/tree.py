def check_pos(array, point):
    #print(f'LEVEL={point[0]} \t WIDTH={point[1]}')
    if(array[point[0]][point[1]] == '#'):
        return 1
    else:
        return 0

with open('input.txt') as reader:
    data = reader.readlines()

data = [x.rstrip() for x in data]

def get_trees(data,move):
    width = len(data[0])-1
    height = len(data)-1
    #print(f'width={width} and {data[0][width]}')
    level=0
    horizontal_pos=0
    trees=0
    while(level<height):
        if(horizontal_pos+move[0] <= width):
            horizontal_pos += move[0]
            level+=move[1]
            #print(f'IF: LEVEL={level} \t WIDTH={horizontal_pos}')
        else:
            level+=move[1]
            diff = horizontal_pos+(move[0]-1) - width
            horizontal_pos = diff
            #print(f'ELSE: LEVEL={level} \t WIDTH={horizontal_pos} \t DIFF={diff}') 
        trees += check_pos(data,[level,horizontal_pos])
    return trees


move=[(3,1),(1,1),(5,1),(7,1),(1,2)]
r=1
for m in move:
    trees = get_trees(data,m)
    r*=trees
    print(f'{trees} and {r}')
