print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            match choice:
                case "1":
                    rows = int(input("Enter the number of rows: "))

                    if rows <= 0:
                        print("Please enter a positive number of rows.")
                        continue

                    print("\nPattern:")

                    for i in range(1, rows + 1):
                        for j in range(i):
                            print("*", end="")
                        print()

                case _:
                    print("Invalid pattern choice.")

        case "2":
            start = int(input("Enter the start of the range: "))
            end = int(input("Enter the end of the range: "))

            if start > end:
                print("Invalid range! End must be greater than or equal to start.")
                continue

            total = 0

            for num in range(start, end + 1):
                if num % 2 == 0:
                    print("Number", num, "is Even")
                else:
                    print("Number", num, "is Odd")

                total = total + num

            print("Sum of all numbers from", start, "to", end, "is:", total)

        case "3":
            print("Exiting the program. Goodbye!")
            break

        case _:
            print("Invalid choice! Please select 1, 2, or 3.")