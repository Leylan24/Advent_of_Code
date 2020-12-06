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
  for entry in array:
    if(entry[0] == valid[0]): #byr
      if(int(entry[1])< 1920 or int(entry[1]) > 2002):
        return False
    else if(entry[0] == valid[1]): #iyr
      if(int(entry[1])< 2010 or int(entry[1]) > 2020):
        return False
    else if(entry[0] == valid[2]): #eyr
      if(int(entry[1])< 2020 or int(entry[1]) > 2030):
        return False
    else if(entry[0] == valid[3]): #hgt
      if(entry[1].find('cm') != -1):
        convert = int(entry[1][:-2])
    else if(entry[0] == valid[4]): #hcl

    else if(entry[0] == valid[5]): #ecl

    else if(entry[0] == valid[6]): #pid

    else:
      print("Fake News")

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
