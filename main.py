frame = int(input("Number of frames: "))

count = 0
memory = []
faults = 0
x = 0

arr = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]

for page in arr:
    if memory.count(page) == 0 and count < frame:
        memory.append(page)
        count += 1
        faults += 1
        print(memory)
    elif memory.count(page) == 0 and count == frame:
        future = -1
        for i in memory:
            if arr[x:].count(i) == 0:
                evictedPage = i
                break
            else:
                index = arr[x:].index(i)
            if index > future:
                future = index
                evictedPage = i
    elif memory.count(page) > 0:
        pass
    x += 1

print(faults)
