import itertools as it

def valid_password(password_,low,high,letter_):
    count = 0
    r=range(low,high)
    for single in password_:
        if(single == letter_):
            #print(single)
            count+=1
    if(low <= count <=high):
        print(f'CORRECT: PASS={password_} \t LETTER={letter_} \t COUNT = {count} \t MIN = {low} \t MAX={high}')
        return 1
    else:
        print(f'INCORRECT: PASS={password_} \t LETTER={letter_} \t COUNT = {count} \t MIN = {low} \t MAX={high}')
        return 0
def valid_password_2(password_,low,high,letter_):
    val_1= password_[low] == letter_
    val_2= password_[high] == letter_
    if(val_1^val_2):
        print(f'val_1= {val_1} and val_2= {val_2} XOR= {val_1^val_2}')
        return 1
    #if(val_1 != val_2 and (val_1 or val_2)):
    #    print(f'CORRECT: WORD={password_}\t LOW_VAL={password_[low-1]} \t HIGH_VAL={password_[high-1]} LOW={low} HIGH={high}')
    #    return 1
    else:
        print(f'INCORRECT: WORD={password_}\t LOW_VAL={password_[low-1]} \t HIGH_VAL={password_[high-1]} LOW={low} HIGH={high}')
        return 0

with open('input.txt') as reader:
    data = reader.readlines()

data =[x.rstrip() for x in data]
valid=0
for line in data:
    val,password = line.split(':')
    bounds_hyphen,letter = val.split(' ')
    bounds=bounds_hyphen.split('-')
    valid= valid+ valid_password_2(password,int(bounds[0]),int(bounds[1]),letter)
    #valid_password_2(password,int(bounds[0]),int(bounds[1]),letter)

#valid = valid_password_2("kqqq",2,3,'q')
print(f'{valid}')


