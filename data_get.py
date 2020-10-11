def data_read() -> dict:
    """This data wrangling script is used to read data into python. \
        The raw data is provided as a csv-file in a subfolder 'data'. \
        Here we preprocess a data set for further use. \
        
        Data description: \
            TBA 
        Data source: \
            TBA <date>

    Returns:
        dict: A key is a year, a value is a float. 
    """
    import csv

    try:
        with open('data/data_raw.csv', mode='r') as infile:
            reader = csv.reader(infile)
            data_dict = {int(rows[0]): float(rows[1]) for rows in reader}
        return data_dict

    except FileNotFoundError as file_error:
        print(file_error, "The data could not be found. The program is closing.", sep='\n')

    except:
        import sys
        print("Unexpected error:", sys.exc_info()[0])
        raise



def main():
    try:
        print("The raw data in dictionary format:", data_read(), sep='\n')
# TODO: Fix so that the above line will NOT be printed if reading the csv file has failed. 

    except NameError as name_error:
        print(name_error, "The data could not be read into dictionary format. The program is closing.", sep='\n')

    except:
        import sys
        print("Unexpected error:", sys.exc_info()[0])
        raise



if __name__ == '__main__':
    main()
