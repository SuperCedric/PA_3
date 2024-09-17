
import pandas as pd

def code():
    # a. load the .csv file into a dataframe named 'cars'
    cars = pd.read_csv('cars.csv')

    # b1. Display the first five rows of the resulting cars
    print("The first five rows are:
")
    print(cars.head())
    
    # b2. Display the last five rows of the resulting cars
    print("The last five rows are:
")
    print(cars.tail())
