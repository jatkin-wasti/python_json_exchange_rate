import json  # importing json so that we can load the json file into a dictionary


# Creating our class
class ExchangeRates:

    # Creating a function to read the json file and return a dictionary with the same information
    def read_file(self):
        with open("exchange_rates.json") as jsonfile:  # Opening the file and aliasing the file name
            rates_dict = json.load(jsonfile)  # load() copies the data and stores into a variable
        return rates_dict  # Returns the dictionary holding all of the json data

    # Creating a function to output the exchange rates by iterating through the dictionary
    def rates_by_country(self):
        rates_dict = self.read_file()
        for key in rates_dict['rates']:
            print(f"€1 is worth {rates_dict['rates'][key]} {key}")


# Creating an instance of the class to test if it works
test = ExchangeRates()
test.rates_by_country()
