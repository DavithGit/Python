"""
PE2 4.3 real files
Assignment: Processing Files

    Open sales_totals in read mode (Download the start file)
    Read each line in a loop
    Strip newline and convert to float
    Add to running total
    Count the lines
    Format and print each number
    Print the total, count, and average
    Use a main() function
    Use try and except for errors

"""

def main():
    total = 0.0
    count = 0

    try:
        with open('sales_totals.txt', 'r') as file:
            for line in file:
                line = line.strip()
                # skip empty lines
                if not line:
                    continue  

                try:
                    amount = float(line)
                except ValueError:
                    print(f"Invalid number found: {line}")
                    continue
                # formatted output
                print(f"{amount:,.2f}")  
                total += amount
                count += 1

        if count == 0:
            print("No valid numbers found.")
            return

        average = (total / count)

        print("\nSummary:")
        print(f"Total:   {total:,.2f}")
        print(f"Count:   {count}")
        print(f"Average: {average:,.2f}")

    except IOError:
        print("IOError: Unable to open the file.")


main()