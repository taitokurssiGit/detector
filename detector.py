# Imports a function 'data_read' from a selfmade module 'data_get' residing in a subfolder 'data'. 
# That function provides some data in a dictionary format into this main program. 
from data.data_get import data_read

data_dict = data_read()

print("Testing the data by printing the value for the year 2000: ", data_dict[2000], sep='\n')

#TODO: code the following functionally without while loop. 

while True:
    x = int(input("Enter a year between 1901–2020: ")) # TODO: 1) Make tests for possible malformated inputs. 2) Remove hard coded years. 
    if data_dict[x] - data_dict[x - 1] > 0:
        print(f"It got BIGGER between {x - 1}–{x}.") # TODO: print also some values (compare also to x-10), e.g. increase in percentage: lambda x: ((data_dict[x] - data_dict[x - 1]) / data_dict[x - 1]) * 100
    else:
        print(f"That was extremely lucky! It got smaller between {x - 1}–{x}.")
    
    again = input("Do you want to test another year? (Y/N): ")

    if again.lower() == "n":
        print("That's the spirit. Good bye!")
        break