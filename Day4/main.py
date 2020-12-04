

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
combined_data = [x.rstrip() for x in combined_data]



