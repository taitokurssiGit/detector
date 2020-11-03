import sys

try:
    from data_get import data_read
    # This function provides some data in a dictionary format into this main program. 
    # The data is described in the function itself. 
    data_dict = data_read()

except ModuleNotFoundError as import_e:
    print(import_e, sep='\n')

except FileNotFoundError as file_error:
    print(file_error, """Check that your current working directory is the same where this detector.py script is located.""", sep='\n')

except:
    print("Unexpected error:", sys.exc_info()[0])
    raise    

else: 
    # Get the available time interval, i.e. the smallest and the biggest keys:
    year_start = min(data_dict.keys())
    year_end = max(data_dict.keys())

    while True:
        x = int(input(f"Enter a year between {year_start + 1}–{year_end}: ")) # TODO: 1) Make tests for possible malformated inputs.
        
        if data_dict[x] - data_dict[x - 1] > 0:
            print(f"It increased between {x - 1}–{x}.") # TODO: print also some values (compare also to x-10), e.g. increase in percentage: lambda x: ((data_dict[x] - data_dict[x - 1]) / data_dict[x - 1]) * 100
        
        ''' else:
            print(f"That was extremely lucky! It decreased between {x - 1}–{x}.") # TODO: When values start to decrease, uncomment and finalize this. '''

        again = input("Do you want to continue? (Y/N): ")

        if again.lower() == "n":
            print("That's the spirit. Good bye!")
            break
