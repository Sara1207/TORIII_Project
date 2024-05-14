def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

# Example usage:
file_path = 'file.txt'  # Replace 'example.txt' with your file path
num_lines = count_lines(file_path)
if num_lines is not None:
    print(f"Number of lines in '{file_path}': {num_lines}")


codeword = '000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
print(len(codeword))