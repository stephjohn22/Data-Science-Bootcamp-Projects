city_flight = input("Which city are you flying to? ")
num_nights = input("How many nights are you staying at your hotel? ")
rental_days = input("How many days do want to hire the car? ")

# Capitalise the first letter of the inputted city
city_flight = str.capitalize(city_flight)
# Change num_nigths from a string to an integer for future calculations
num_nights = int(num_nights)
# Change rental_days from a string to an integer for future calculations
rental_days = int(rental_days)

# Confirming details of user input
print(f"You will be staying in {city_flight} for {num_nights} nights and will be hiring a car for {rental_days} days.")

# Calculating the cost of hotel for the total stay
def hotel_cost(num_nights):
    # Fixed cost of one night in hotel
    cost_per_night = 170
    total_hotel_cost = num_nights * cost_per_night
    return total_hotel_cost

print(f"The cost of {num_nights} nights at your chosen hotel is £{hotel_cost(num_nights)}.")

# Cost of flight depending on the user input for city_flight
def plane_cost(city_flight):
    if city_flight == "Paris":
        return 95
    elif city_flight == "Rome":
        return 160
    elif city_flight == "Madrid":
        return 155
    elif city_flight == "Lisbon":
        return 250
    elif city_flight == "Brussels":
        return 115
    else:
        return 350

print(f"The cost of a return flight from London to {city_flight} is £{plane_cost(city_flight)}.")

def car_rental(rental_days):
    # Fixed cost of renting a car for one day
    daily_rental_cost = 30
    total_rental_cost = rental_days * daily_rental_cost
    return total_rental_cost

print(f"The cost to rent a car for {rental_days} days is £{car_rental(rental_days)}.")

# Calculating the total cost of hotel, flight and car rental
def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)

print(f"The total cost of your holiday to {city_flight} is £{holiday_cost(hotel_cost, plane_cost, car_rental)}.")