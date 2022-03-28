# List of all items on menu
menu = ['Burger','Chips','Coke','Ice cream']

# Dictionary of all prices of the items on menu
stock = {'Burgers': 10,
         'Chips': 30,
         'Coke': 50,
         'Ice cream': 20,
         }

# Dictionary of all stock levels of the items on menu
price = {'Burgers': 32,
         'Chips': 18,
         'Coke': 12,
         'Ice cream': 19,
         }

# Variable that is storing value of items
total_value = 0

# For loop that calculates the total value of items
for i in stock:
        total_value = total_value + (stock[i] * price[i])

# Prints the results of the for loop
print(total_value)