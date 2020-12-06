def optimal_page_replacement():
    arr = []
    a = input("Enter a reference string: ")
    for i in range(len(a)):
        arr.append(int(a[i]))  # convert user entry into int list
    frame = int(input("Enter the # of frames: "))
    page_faults = 0
    asterisk = '*'
    opr = [asterisk] * frame  # new list with * and length specified by user

    print("\nRunning simulation: ")
    print(f"\nStart: Memory is: {' '.join(map(str, opr))}")

    for number_in_array in range(len(arr)):
        questionable_element = 0
        for index_in_frame in range(frame):
            if opr[index_in_frame] == arr[number_in_array]:
                questionable_element = 1
                break

        if questionable_element == 0:
            is_it_fault = False
            position = asterisk
            for element in range(frame):
                if opr[element] == asterisk:
                    is_it_fault = True
                    position = element

            if not is_it_fault:
                furthest_out = 0
                most_furthest_out = asterisk
                for element in range(frame):
                    if opr[element] != asterisk:
                        found = False  # element we're trying to put in is not in the page
                        for m in range(number_in_array,
                                       len(arr)):  # look for number from position until the end of array
                            if arr[m] == opr[element]:
                                found = True
                                if m > furthest_out:
                                    furthest_out = m
                                    most_furthest_out = element
                                break
                        if not found:
                            most_furthest_out = element
                            break

                position = most_furthest_out

            page_faults += 1
            opr[position] = arr[number_in_array]
            print(f"{arr[number_in_array]}: Memory is: {' '.join(map(str, opr))[::-1]}: "
                  f"Page Fault: (Number of Page Faults: {page_faults})")

        else:
            print(f"{arr[number_in_array]}: Memory is: {' '.join(map(str, opr))[::-1]}: "
                  f"Hit: (Number of Page Faults: {page_faults})")

    print(f"Total Number of Page Faults: {page_faults}")


optimal_page_replacement()
