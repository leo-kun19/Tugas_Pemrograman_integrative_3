def read_integers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            numbers = [int(line.strip()) for line in file]
        return numbers
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

def print_sum_with_comma_separator(numbers):
    total = sum(numbers)
    formatted_total = "{:,.2f}".format(total)
    print(formatted_total)

# Main code
if __name__ == "__main__":
    integers = read_integers_from_file("indata.txt")
    if integers:
        print_sum_with_comma_separator(integers)
