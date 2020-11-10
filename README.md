# Task
## Use a Json file to show exchange rates by country
- Create a new github Repo
- .gitignore and README in a new pycharm project
- have the exchange_rates.json file available in your pycharm project
- Display all of the data from the .json file
- Iterate through the data and display exchange rate by country
## Solution
### Downloading Json file
- To be able to use the information stored in a json file we have to have access to it. Make sure you have a json file 
storing the same information as in my ```exchange_rats.json``` file. One way to accomplish this is creating a new json 
in your new pycharm project and copying + pasting the json file in this github repo
### Creating your class and methods
- As stated above, we need to retrieve information from a json file, therefore we should import json at the top of our 
python file
```
import json  # importing json so that we can load the json file into a dictionary
```
- Create our class to store the functionality to accomplish the task
```
# Creating our class
class ExchangeRates:
```
- Now we'll create a method to open the json file and store the information in a dictionary that we are calling 
```rates_dict```
- We will return this variable so that we can use it in our next method
```
    # Creating a function to read the json file and return a dictionary with the same information
    def read_file(self):
        with open("exchange_rates.json") as jsonfile:  # Opening the file and aliasing the file name
            rates_dict = json.load(jsonfile)  # load() copies the data and stores into a variable
        return rates_dict  # Returns the dictionary holding all of the json data
```
- Now we need to actually do something with the data we just retrieved
- We're going to call the previous function and store the variable returned as a 
- We have to do this as rates_dict is only defined in local scope, meaning that we can only use it in the method that 
created it (in this case that's the read_file method)
- We then loop through the dictionary using the key (currency) and output the value for that key (how much one euro is 
worth in that currency)
```
    # Creating a function to output the exchange rates by iterating through the dictionary
    def rates_by_country(self):
        rates_dict = self.read_file()
        for key in rates_dict['rates']:
            print(f"€1 is worth {rates_dict['rates'][key]} {key}")

```
- To run the methods we will create an instance of the class and run the rates_by_country method
```
# Creating an instance of the class to test if it works
test = ExchangeRates()
test.rates_by_country()
```
- When run, this nicely outputs the exchange rates for each country. Good job!
