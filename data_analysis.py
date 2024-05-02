# some beginning examples for data analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

number_list = [1, 45, 99, 4.3]
string_list = ["a", "d", "something", "else"]
mixed_list = [45, "d", 89.33, "something"]

number_array = np.array(number_list)
print(number_array)
type(number_array)
number_array.dtype

string_array = np.array(string_list)
print(string_array)
type(string_array)
string_array.dtype

mixed_array = np.array(mixed_list)
print(mixed_array)
type(mixed_array)
mixed_array.dtype

# what's the point of an array

fruit_dictionary = {"apples" : 3.49,
                    "bananas" : 1.79,
                    "strawberries" : 5.99}

fruit_tax = 0.1

fruit_prices = list(fruit_dictionary.values())
print(fruit_prices)

taxed_prices = []
for price in fruit_prices:
    taxed_price = round(price * (1 + fruit_tax), 2)
    taxed_prices.append(taxed_price)
print(taxed_prices)

# list comprehension example
# new_list = [thing_to_get_new_list_member for var in iter]
taxed_prices2 = [round(price * (1 + fruit_tax), 2) for price in fruit_prices]
print(taxed_prices2)

# best with numpy array
taxed_prices3 = np.array(fruit_prices) * (1 + fruit_tax)
print(taxed_prices3)
taxed_prices3 = taxed_prices3.round(2)
print(taxed_prices3)

# another handy thing: arange()
range(10)
np.arange(10) * 2
np.arange(3, 12)
np.arange(3, 28, 3)

######################################
# Data Frames
fruit_dictionary = {"apples" : 3.49,
                    "bananas" : 1.79,
                    "strawberries" : 5.99}

fruit_names = list(fruit_dictionary.keys())

fruit_data = {"fruit" : fruit_names,
              "price" : fruit_prices}
print(fruit_data)

fruit_dataframe = pd.DataFrame(data = fruit_data)
print(fruit_dataframe)

fruit_data["price"]
fruit_dataframe["price"]
type(fruit_dataframe["price"])

fruit_dataframe["price"] * (1 + fruit_tax)

fruit_dataframe.describe()
fruit_dataframe["price"].mean()
fruit_dataframe["price"].min()
fruit_dataframe["price"].max()

