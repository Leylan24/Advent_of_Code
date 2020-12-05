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
      print(passport.find(word))
      return 0
  return 1


valid_count=0
for passport in combined_data:
  print(passport)
  valid_count+=check_passport(passport)
  print(f'<-----{valid_count}------>')
       
print(valid_count)

