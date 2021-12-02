file = open("input.txt", "r")
lines = file.readlines()
lines = [line.rstrip("\n") for line in lines]

increase = 0
for next_index,depth in enumerate(lines,0):
  next_index+=1
  print(f"Prev:{depth} Next:{lines[next_index]}")
  if int(depth) < int(lines[next_index]):
    print(f"Increasing: {increase}")
    increase+=1
  if next_index == len(lines)-1:
    break

print(increase)
