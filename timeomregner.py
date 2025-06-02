def time_to_float(time_str):
    hours = int(time_str[:-2])
    minutes = int(time_str[-2:])
    return hours + minutes / 60

booli = True
while booli:
    start_time = input("Enter the start time: ")
    end_time = input("Enter the end time: ")

    start_float = time_to_float(start_time)
    end_float = time_to_float(end_time)
    total_time = end_float - start_float

    print("Total time:", total_time)
    print("Total tid minus pause:", total_time - 0.5)
    print("...")
    valg = input("Trykk 9 for å avslutte \nEnter for å fortsette ")
    if valg == 2:
        booli = False