valid = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

with open('input.txt') as reader:
    data = reader.readlines()


buffer_ = ""
combined_data=[]
for line in data:
    if(line == '\n'):
        combined_data.append(buffer_)
        buffer_= ""
    else:
        buffer_ =buffer_ + line
combined_data.append(buffer_) #forgot about last one
#combined_data = [x.rstrip() for x in combined_data]

def check_passport(passport):
  for word in valid:
    if(passport.find(word)==-1):
      return False
  return True
def check_data(array):
    print("<------NEW-------->")
    for entry in array:
        print(f'---------{entry}---------------')
        if(entry[0] == valid[0]): #byr
            if(int(entry[1])< 1920 or int(entry[1]) > 2002):
                print("***byr false")
                return False
        elif(entry[0] == valid[1]): #iyr
            if(int(entry[1])< 2010 or int(entry[1]) > 2020):
                print("***iyr false")
                return False
        elif(entry[0] == valid[2]): #eyr
            if(int(entry[1])< 2020 or int(entry[1]) > 2030):
                print("***eyr false")
                return False
        elif(entry[0] == valid[3]): #hgt
            if(entry[1].find('cm') ==-1 and entry[1].find('in')==-1):
                return False
            convert = int(entry[1][:-2])
            if(entry[1].find('cm') != -1):
                if(convert<150 or convert >193):
                    print("***hgt cm false")
                    return False
            if(entry[1].find('in') != -1):
                if(convert<59 or convert >76):
                    print("***hgt in false")
                    return False
        elif(entry[0] == valid[4]): #hcl
            if(entry[1][0] != '#'):
                print("***hcl hashtag false")
                return False
            if(len(entry[1][1:])!=6):
                print("***hcl not 6 false")
                return False
            var = entry[1][1:4]
            
            for n in var:
                if(n.isdigit()):
                    if int(n) not in range(0,10):
                        print("***Not in range number")
                        return False
                else:
                    if n > 'f':
                        print("***Not in range letter")
                        return False
        elif(entry[0] == valid[5]): #ecl
            valid_eye = ['amb','blu','brn','gry','grn','hzl','oth']
            if entry[1] not in valid_eye:
                print('***Eye colour not found')
                return False
            #print(entry[1])
        elif(entry[0] == valid[6]): #pid
            if(len(entry[1])!=9):
                print("***pid length incorrect")
                return False
    print("RETURN TRUE")    
    return True

#valid_count=0
valid_passports=[]
for passport in combined_data:
  if(check_passport(passport)):
       valid_passports.append(passport)

# Fucking unncessacry in my opinion but it works
valid_passports = [x.replace('\n',' ') for x in valid_passports]
valid_passports = [x.split() for x in valid_passports]
valid_passports = [[y.split(':') for y in x] for x in valid_passports]
#valid_passports = [valid_passports.remove(passports) if(check_data(passports)==False) for passports in valid_passports]
count=0
for passports in valid_passports:
    print(check_data(passports))
    if(check_data(passports)==True):
        count+=1
        print(f'COUNTE == {count}')
print(f'<---------------{count}------------------->')
            
