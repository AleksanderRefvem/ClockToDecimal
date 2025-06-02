def time_to_float(time_str):
    # Konverterer klokkeslett i formatet HHMM til desimaltall (timer)
    hours = int(time_str[:-2])      # Henter ut timer fra de første sifrene
    minutes = int(time_str[-2:])    # Henter ut minutter fra de to siste sifrene
    return hours + minutes / 60     # Returnerer tid som desimaltall

booli = True
while booli:
    # Tar inn start- og sluttidspunkt fra bruker
    print("Please input a time (e.g. 10.00 -> 1000)")
    start_time = input("Enter start time: ")
    end_time = input("Enter end time: ")

    # Konverterer tidene til desimaltall
    start_float = time_to_float(start_time)
    end_float = time_to_float(end_time)
    total_time = end_float - start_float  # Regner ut total tid

    print("")
    print("Total time:", total_time)  # Skriver ut total tid
    print("Total time minus break (30 minutes):", total_time - 0.5)  # Skriver ut tid minus 0.5 time pause
    print("...")
    try:
        valg = int(input("Press 9 to exit or Enter to continue "))
        if valg == 9:  # Sjekker om bruker vil avslutte
            booli = False
    except ValueError:
        # Hvis brukeren ikke skriver inn et tall, fortsetter vi bare
        print("Wrong input format. Program continues.")
        pass

print("Goodbye.")