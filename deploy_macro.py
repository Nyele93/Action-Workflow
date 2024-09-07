from typing import List

l: list[int] = [10, 20, 25, 35, 85]
ny: list[str] = ['10', '20', '25', '35', '85']
print(l[0:3])
result = ', '.join(ny)
print(result)

print(len(l))

start_index = 1
cell_len = 25
for i in range(cell_len - 1, start_index - 1, -1):
    current_cell = i
    next_cell = i + 1
    print(current_cell, next_cell)

rng = range(0, 11)
for i in rng:
    print(i)


#report_dir=/home/michael
# Command to execute
#command = "cd report_dir"
# Run the command and capture the output
#output = subprocess.check_output(command, shell=True)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('This is a test Python Program!')
    #type(10)
