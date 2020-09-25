# Imports a function 'data_read' from a module 'data_get'. 
#                       TODO: ...from a module 'data_get' residing in a subfolder 'data'. 

try:
    from data_get import data_read # or: from data.data_get import data_read
    # This function provides some data in a dictionary format into this main program:
    data_dict = data_read()

except ModuleNotFoundError as import_e:
    print(import_e, sep='\n')

except FileNotFoundError as file_error:
    print(file_error, """Check that your current folder is the same where this detector.py script is located. 
    Launch the program there by commanding
    python detector.py""", sep='\n')

except:
    import sys
    print("Unexpected error:", sys.exc_info()[0])
    raise    

else:
    #TODO: code the following functionally without while loop?

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