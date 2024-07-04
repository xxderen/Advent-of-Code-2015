with open("day2.txt", "r") as f:
    lines = f.read().splitlines()
wrapping_paper = 0
ribbon = 0
for entry in lines:
    entry = entry.split("x")
    l = int(entry[0])
    w = int(entry[1])
    h = int(entry[2])
    wrapping_paper += 2*l*w+2*w*h+2*h*l
    wrapping_paper += min(l*w,w*h,h*l)
    ribbon += l*w*h
    if min(l,w,h) == l:
        second_min = min(w,h)
    elif min(l,w,h) == w:
        second_min = min(l,h)
    elif min(l,w,h) == h:
        second_min = min(l,w)
    ribbon += 2*min(l,w,h)+2*second_min
print(ribbon)
print(wrapping_paper)