# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

def km_conv(miles):
    km = miles * 1.6
    return km

def travel_cost_km(miles, cost_per_km):
    km_cost = km_conv(miles) * cost_per_km
    return km_cost

def hotel_cost(num_nights, h_rate):
    h_cost = num_nights * h_rate
    return h_cost

def total_trv_cost(miles, cost_per_km, num_nights, h_rate):
    tot_cost = travel_cost_km(miles, cost_per_km) + hotel_cost(num_nights, h_rate)
    return tot_cost

cost = total_trv_cost(200, 2, 5, 50)
print(f"Your total trip cost is GBP {cost}")
