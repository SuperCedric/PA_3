
import pandas as pd

def code():
    # a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.
    print("The first five rows with odd-numbeed columns are: ")
    print(cars.iloc[:5,::2])

    # b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
    print("
The row that contains the model of Mazda RX4 is:")
    print(cars[cars['Model'] == 'Mazda RX4'])

    # c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
    print("
The model Camarzo Z28 has this many cylinders:")
    print(cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0])

    # d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
    print("
The number of cylinders and type of gears of Mazda RX4 Wag, Ford Pantera L, and Honda Civic are:")
    print(cars.loc[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']), ['Model', 'cyl', 'gear']])
