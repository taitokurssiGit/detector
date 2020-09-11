# Imports a function from a subfolder to provide data in dictionary format into this program: 
from data.data_get import data_read

data_dict = data_read()

# Minor problem: keys are not integers.
# TODO: How to convert keys from str to int?
print(data_dict['2000'])

# TODO: a neat loop: 
i = 1
while i != 0:
    i = input("Enter a year or quit by entering 0: ")
    if float(data_dict[i]) - float(data_dict[str(int(i) - 1)]) > 0:
        print("It's getting bigger")
