<a name="top"></a>

# PA 3: PYTHON DATA ANALYSIS
This repository includes my solution to the two given problems involving the Pandas library. Respectively, the first and second problem are named *Problem 1* and *Problem 2*

### GIVEN PROBLEMS ###
#### 1. Problem 1 ####
  - In this problem, we are tasked to load a dataframe from a given downloadable file named `cars.csv`. Additionally, we are tasked to display the first and last 5 rows in the dataframe.
#### 2. Problem 2 #### 
  - In this problem, we are given 5 tasks. First is to display the first five rows that include only the odd-numbered columns. Next, identify and display the row corresponding to the car model named `Mazda RX4` to examine its details. Following this, determine the number of cylinders `cyl` for the car model `Camaro Z28` to understand its engine specification. Additionally, find out both number of cylinders `cylc` and the gear type `gear` for the specific car models: `Mada RX4 Wag`, `Ford Pantera L`, and `Honda Civic`.

## DEPENDENCIES ##
Importing the pandas library is crucial in order to use its functions 
```
import pandas as pd
```

## LOADING OF CAR.CSV ##
To take the `csv` file, the function `pd.read_csv()` must be used. This data will be used for both problems. 
```python
import pandas as pd

#read the .csv file and store it in variable cars for ease of accessibility
cars = pd.read_csv('cars.csv')
#Print the dataframe to check if function worked properly
cars
```
  - Notes
    - Ensure that the `cars.csv` file is in the correct directory before running the script. 

## 1️⃣ PROBLEM 1 ##
The goal for this problem is to load the data into a pandas dataframe and perform basic data exploration tasks. Specifically, we will display the first five and last five rows of the dataset to get an initial understanding of its structure and contents.

### DOCUMENTATION ###
This python script loads a csv file named `cars.csv` and uses the `pd.read_csv()` function to read the file and the `head()` and `tail()` methods to show the top and bottom five rows. The script provides a quick preview of the data for intial exploration and helps verify the file contents.


## CODE ##
```python
import pandas as pd

# a. load the .csv file into a dataframe named 'cars'
cars = pd.read_csv('cars.csv')

# b1. Display the first five rows of the resulting cars
print("The first five rows are:\n")
print(cars.head())
# b2. Display the last five rows of the resulting cars
print("The last five rows are:\n")
print(cars.tail())
```
## OUTPUT ##
```
The first five rows are:
               Model   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear   carb
0          Mazda RX4  21.0    6  160.0  110  3.90  2.620  16.46   0   1     4      4
1      Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4      4
2         Datsun 710  22.8    4  108.0   93  3.85  2.320  18.61   1   1     4      1
3     Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0     3      1
4  Hornet Sportabout  18.7    8  360.0  175  3.15  3.440  17.02   0   0     3      2


The last five rows are:
             Model   mpg  cyl   disp   hp  drat     wt  qsec  vs  am  gear   carb
27    Lotus Europa  30.4    4   95.1  113  3.77  1.513  16.9   1   1     5      2
28  Ford Pantera L  15.8    8  351.0  264  4.22  3.170  14.5   0   1     5      4
29    Ferrari Dino  19.7    6  145.0  175  3.62  2.770  15.5   0   1     5      6
30   Maserati Bora  15.0    8  301.0  335  3.54  3.570  14.6   0   1     5      8
31      Volvo 142E  21.4    4  121.0  109  4.11  2.780  18.6   1   1     4      2

```


### 2️⃣ PROBLEM 2 ##
In this task, we are working with a dataset to perform a series of data analysis operations, namely slicing, subsetting, and indexing to understand their specifications. These tasks will help in better understanding the structure and features of the cars in the dataset.

### DOCUMENTATION ###
This python script used the pandas library to perform data extraction tasks from a dataframe named `cars`. It uses the `iloc()` function to display the odd-numbered columns, the `cars

## CODE ##
```python
import pandas as pd

# a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.
print("The first five rows with odd-numbeed columns are: ")
print(cars.iloc[:5,::2])

# b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
print("\nThe row that contains the model of Mazda RX4 is:")
print(cars[cars['Model'] == 'Mazda RX4'])

# c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
print("\nThe model Camarzo Z28 has this many cylinders:")
print(cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0])

# d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
print("\nThe number of cylinders and type of gears of Mazda RX4 Wag, Ford Pantera L, and Honda Civic are:")
print(cars.loc[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']), ['Model', 'cyl', 'gear']])
```
## OUTPUT ##
```
The first five rows with odd-numbeed columns are: 
               Model  cyl   hp     wt  vs  gear
0          Mazda RX4    6  110  2.620   0     4
1      Mazda RX4 Wag    6  110  2.875   0     4
2         Datsun 710    4   93  2.320   1     4
3     Hornet 4 Drive    6  110  3.215   1     3
4  Hornet Sportabout    8  175  3.440   0     3

The row that contains the model of Mazda RX4 is:
       Model   mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb
0  Mazda RX4  21.0    6  160.0  110   3.9  2.62  16.46   0   1     4     4

The model Camarzo Z28 has this many cylinders:
8

The number of cylinders and type of gears of Mazda RX4 Wag, Ford Pantera L, and Honda Civic are:
             Model  cyl  gear
1    Mazda RX4 Wag    6     4
18     Honda Civic    4     4
28  Ford Pantera L    8     5
```

## SAVING PROBLEM 1 TO .PY FILE ##

### DOCUMENTATION ###
This script demonstrates a way to save the code for problem 1 as a string, store it in a variable, and write it to the `.py` file named `Taguba-Pandas-P1.py`. The code also includes a check to verify whether the content has been successfully saved to the file.
## CODE ##
```python
#Save the code as a string and store it in variable named 'code1'"
code1 = """
import pandas as pd

def code():
    # a. load the .csv file into a dataframe named 'cars'
    cars = pd.read_csv('cars.csv')

    # b1. Display the first five rows of the resulting cars
    print("The first five rows are:\n")
    print(cars.head())
    
    # b2. Display the last five rows of the resulting cars
    print("The last five rows are:\n")
    print(cars.tail())
"""
#Type a command to write the code into a '.py' file so it will be saved into that file
with open('Taguba_Pandas-P1.py', 'w') as file:
    file.write(code1)

#Open the file to check if the content is present
with open('Taguba_Pandas-P1.py', 'r') as file:
    file_contents = file.read()

#If the code is not present in the .py file, print out that it hasn't been saved, but if it is present, print that it has been saved
if 'def code():' in file_contents:
    print("The code has been saved to 'Taguba_Pandas-P1.py'")
else:
    print("The code has NOT been saved to 'Taguba_Pandas-P1.py'")
```
## OUTPUT ##
```
The code has been saved to 'Taguba_Pandas-P1.py'
```
## SAVING PROBLEM 2 TO .PY FILE ##

### DOCUMENTATION ###
This script demonstrates a way to save the code for problem 1 as a string, store it in a variable, and write it to the `.py` file named `Taguba-Pandas-P2.py`. The code also includes a check to verify whether the content has been successfully saved to the file.
## CODE ##
```python
#Save the code as a string and store it in variable named 'code2'"
code2 = """
import pandas as pd

def code():
    # a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.
    print("The first five rows with odd-numbeed columns are: ")
    print(cars.iloc[:5,::2])

    # b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
    print("\nThe row that contains the model of Mazda RX4 is:")
    print(cars[cars['Model'] == 'Mazda RX4'])

    # c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
    print("\nThe model Camarzo Z28 has this many cylinders:")
    print(cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0])

    # d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
    print("\nThe number of cylinders and type of gears of Mazda RX4 Wag, Ford Pantera L, and Honda Civic are:")
    print(cars.loc[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']), ['Model', 'cyl', 'gear']])
"""
#Type a command to write the code into a '.py' file so it will be saved into that file
with open('Taguba_Pandas-P2.py', 'w') as file:
    file.write(code2)

#Open the file to check if the content is present
with open('Taguba_Pandas-P2.py', 'r') as file:
    file_contents = file.read()

#If the code is not present in the .py file, print out that it hasn't been saved, but if it is present, print that it has been saved
if 'def code():' in file_contents:
    print("The code has been saved to 'Taguba_Pandas-P2.py'")
else:
    print("The code has NOT been saved to 'Taguba_Pandas-P2.py'")
```
## OUTPUT ##
```
The code has been saved to 'Taguba_Pandas-P2.py'
```

## BUILT WITH ## 
  - Jupyter Notebook

## LIBRARIES USED ## 
  - PYTHON
       - Pandas
## AUTHOR ##
  - Cedric Kurt Taguba - [@SuperCedric](https://github.com/SuperCedric)

<p align="right">(<a href="#top">[🔼GO TO TOP]</a>)</p>
