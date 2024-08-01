# Items sold represented in a list
menu = ['pizza', 'burger', 'lasagna', 'curry']

# Stock value of each item represented in a dictionary
stock = {
    'pizza': 6, 
    'burger': 10, 
    'lasagna': 14, 
    'curry': 15
}

# Price of each item represented in a dictionary
price = {
    'pizza': 10.50,
    'burger': 13.00,
    'lasagna': 18.00, 
    'curry': 20.50
}

# Calculating the total stock worth
total_stock = 0

for item in menu:
    item_value = stock[item] * price[item]
    total_stock += item_value

print(f"The total stock worth in the cafe is £{total_stock: .2f}")