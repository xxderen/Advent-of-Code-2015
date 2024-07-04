with open("day1.txt", "r") as f:
    lines = f.read()
result = 0
for i in range(0,len(lines)):
    if lines[i] == "(":
        result += 1
    elif lines[i] == ")":
        result -= 1
print(result)

result = 0
index = 0
for i in range(0,len(lines)):
    if lines[i] == "(":
        result += 1
        index += 1
        if result == -1:
            break
    elif lines[i] == ")":
        result -= 1
        index += 1
        if result == -1:
            break
print(index)