"""
This script will show how to use loops.
"""

# basic for loop
for i in range(0,10):
    print(i)

# while version
# use Ctrl+c to kill an infinite loop
print("Running the while loop")
i = 0
while i < 10:
    print(i)
    i += 1

# iterate over a list
my_list = ['a', 'b', 'c']

print("--- running loop over a list ---")
for item in my_list:
    print(item)

# use a while loop instead
print("--- running a while loop on the list ---")
i = 0
while i < len(my_list):
    print(f'Element {i} is {my_list[i]}')
    i += 1

# nested statements
print('--- nested statements ---')
for i in range(0, 20):
    # print(f'i = {i}') # debug statement
    remainder = i % 2
    # print(remainder) # debug statement

    # != --> tests not-equal-to
    if remainder != 0:
        print(f'{i} is an odd number')