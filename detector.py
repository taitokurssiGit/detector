# Imports a function data_read from a selfmade module 'data_get' residing in a subfolder 'data'. 
# This function provides some data in a dictionary format into this main program: 
from data.data_get import data_read

data_dict = data_read()

# Minor problem: keys are not integers. TODO: How to convert keys from str to int?
print("Testing the data by printing the value for the year 2000: ", data_dict['2000'], sep='\n')

while True:
    i = input("Enter a year between 1901–2020: ") # TODO: test the input. 
    if float(data_dict[i]) - float(data_dict[str(int(i) - 1)]) > 0:
        print(f"It's getting BIGGER between {int(i) - 1}–{i}.")
    else:
        print(f"It's getting smaller between {int(i) - 1}–{i}.")
    
    decision = input("Do you want to test another year? (Y/N): ")

    if decision == ("N" or "n"):
        print("Program has been terminated.")
        break
