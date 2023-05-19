'''
Production level code practices
1. break down the code
2. start using a proper IDE
3. group files on the basis of tasks/steps
4. use config.py for all your directories: make config files for all environments
5. use blueprints for flask
6. try to optimize your code as much as possible
7. logging critical failures and intermediate results
8. handle possible errors in the code: use try and except statements to handle possible errors and log them using traceback
9. proper naming to improve readability


'''
# 7.
# define a path for your log file
logs_file_path = "./app.log"

# create the log file
sys.stdout = open(logs_file_path, "w", buffering = 1, encoding = "utf-8")

# this file will contain all the print statements in your application and will display the error tracebacks

# 8. 
import traceback
import sys

logs_file_path = "./app.log"
sys.stdout = open(logs_file_path, "w", buffering = 1, encoding = "utf-8")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year":1964
}

try:
  print(thisdict["car"])
except Exception as i:
  print(traceback.format_exc())

  
  
names = ["Mukesh", "Roni", "Chari"]
ages = [24, 50, 18]
for i, (name, age) in enumerate(zip(names, ages)):
  print(i, name, age)
  
stocks = ["GEEKS", "For", "geeks"]
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks, prices in zip(stocks, prices)}
print(new_dict)

# unzip
mapped = zip(name, roll_no, marks)
mapped = list(mapped)
namz, roll_noz, marksz = zip(*mapped)

'''
IDE: Integrated Development Environment
There can be a configuration file that has all the directories, paths, and values/strings that have to be hard-coded, and a helpler file or a loading file that would ahve all the specific functions for loading files from thoese directories. 

The __init__.py files are required to make Python treat directories containing the file as packages. 

Python zip() method takes iterable containers and returns a single iterator object, having mapped values from all the containers. 
It is used to map the similar index of multiple containers so that they can be used just using a single entity. 

enumerate() function is used to iterate over an iterable and return both the index and corresponding element at that index. It is often used in for loops to keep track of the index of the current iteration. 

The combination of zip() and enumerate() is useful in scenarios where you want to process multiple lists or tuples in parallel, and also need to access their indices for any specific purpose. 

'''


# 10 advanced concepts in Python
'''
1. map(function, iterable)


2. itertools


3. lambda function


4. exception handling


5. decorators

 
6. collections


7. generators


8. magic methods


9. threading


10. Regular expressions
'''
