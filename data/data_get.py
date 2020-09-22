def data_read() -> dict:
    """This script is used to read data into python. The data is provided as a csv-file. 

    Returns:
        dict: A key is a year, a value is a float. 
    """
    import csv

    with open('./data_raw.csv', mode='r') as infile:
        reader = csv.reader(infile)
#        with open('data_raw_new.csv', mode='w') as outfile:
#            writer = csv.writer(outfile)
        data_dict = {int(rows[0]): float(rows[1]) for rows in reader}
    return data_dict