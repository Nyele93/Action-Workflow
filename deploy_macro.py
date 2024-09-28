import json
from typing import List

l: list[int] = [10, 20, 25, 35, 85]
ny: list[str] = ['10', '20', '25', '35', '85']

# Prepare output as a dictionary
output = {
    "first_3_elements": l[0:3],
    "joined_list": ', '.join(ny),
    "list_length": len(l),
    "cell_ranges": [(i, i+1) for i in range(24, 0, -1)],
    "range_values": list(range(0, 11)),
    "greeting": 'Hi, This is a test Python Program!'
}
#report_dir=/home/michael
# Command to execute
#command = "cd report_dir"
# Run the command and capture the output
#output = subprocess.check_output(command, shell=True)
 #type(10)

#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Write JSON to a file
with open('py_output.json', 'w') as f:
    json.dump(output, f, indent=4)

# Optionally print the output
#print(json.dumps(output, indent=4))

# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('This is a test Python Program!')
