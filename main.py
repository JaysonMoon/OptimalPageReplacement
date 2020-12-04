# arr = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
# frame = int(input("Enter number of frames: "))
# opr = []
# remainder = [None for i in range(frame)]
# page_faults = 0
# print(f"Start: Memory is: {opr}")
#
# # for i in range(len(arr)):
# #     if arr[i] not in opr:
# #         if len(opr) < frame:
# #             page_faults += 1
# #             opr.append(arr[i])
# #             print(f'{arr[i]}: Memory is: {opr}: # of Page Fault(s): {page_faults}')
# #         else:
# #             for j in range(len(arr)):
# #                 if opr[j] not in arr[i + 1:]:  # if target element is not in the rest of array, replace it
# #                     opr[j] = arr[i]
# #                     break
# #                 else:
# #                     page_faults += 1
# #                     opr[j] = arr[i + 1:].index([remainder[j]])
# # print(opr)

f = []
fault = 0
pf = 'No'
storage = int(input("Enter frames: "))

for i in range(storage):
    occurrence = [None for i in range(storage)]

for i in range(storage):
    if storage[i] not in f:
        if len(f) < storage:
            f.append(storage[i])
        else:
            for x in range(len(f)):
                if f[x] not in storage[i+1]:
                    f[x] = storage[i]
                    break
                else:
                    occurrence[x] = storage[i+1:].index(f[x])
            else:
                f[occurrence.index(max(occurrence))] = storage[i]
print('hello world')