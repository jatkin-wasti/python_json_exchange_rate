import json


class ExchangeRates:

    def read_file(self):
        with open("exchange_rates.json") as jsonfile:
            rates_dict = json.load(jsonfile)  # load() copies the data and stores into a variable
        return rates_dict


    def rates_by_country(self):
        rates_dict = self.read_file()
        for key in rates_dict['rates']:
            print(f"€1 is worth {rates_dict['rates'][key]} {key}")


test = ExchangeRates()
test.rates_by_country()
