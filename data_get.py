import sys, csv#, requests

'''TODO: 
1) Miten ladataan netistä csv-tiedosto? 

2) Onko tässä liikaa try-except-rakenteita? Ovatko ne epärelevanteja. Toimivat huonosti. 
    Olisiko jotain hyödyllisiä os.path-metodeja?

3) 
# TODO: Katsotun Youtube-videon perusteella:
# Tee setUpClass, jolla luetaan file kertaalleen, ennen kaikkia testimetodeja. 
# HUOM: jos website on alhaalla! Tee mocking: 
#   response = requests.get(f'LÄHDE-URL-TÄHÄN')
# Mihin kohtaan se tulisi: omana funktiona vaiko main():n alle: 

'''

def data_read() -> dict:
    """This data wrangling script is used to read data for Python. The raw data is \
        provided as a csv-file in a subfolder 'data'. Here we preprocess a data set for further use.

    Data description: \
        Annual average atmospheric carbon dioxide (CO2) contents expressed as \
        a mole fraction in dry air, micromol/mol, commonly abbreviated as \
        ppm (parts per million). For example, 413 ppm means that in every \
        million molecules of (dry) air there are on average 413 molecules of CO2.\
        Info and more data: https://www.esrl.noaa.gov/gmd/ccgg/trends/data.html

    Data source: \
            Dr. Pieter Tans, NOAA/GML (www.esrl.noaa.gov/gmd/ccgg/trends/) and Dr. Ralph Keeling, \
                Scripps Institution of Oceanography (scrippsco2.ucsd.edu/). \
            Mauna Loa CO2 annual mean data (CSV), \
                ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_annmean_mlo.csv, \
                downloaded on 2020-10-27.

    Returns:
        dict: A key is a year, a value is a float of CO2 mole fraction in dry air (micromol/mol or ppm).
    """

    try:
        with open('data/co2_annmean_mlo.csv', mode='r') as infile:
            reader = csv.reader(filter(lambda row: row[0]!='#', infile))
            header_line = next(reader)
            data_dict = {int(rows[0]): float(rows[1]) for rows in reader} # TODO: How catch the third value from csv, i.e. "unc 0.12"? 
        return data_dict

    # except FileNotFoundError as file_error:
    #     print(file_error, "The data could not be found. The program is closing.", sep='\n')

    except:
       print("Unexpected error:", sys.exc_info()[0])
       raise



def main():
    try:
        print("The data in dictionary format:", data_read(), sep='\n')

    except NameError as name_error:
        print(name_error, "The data could not be read into dictionary format. The program is closing.", sep='\n')



if __name__ == '__main__':
    main()
