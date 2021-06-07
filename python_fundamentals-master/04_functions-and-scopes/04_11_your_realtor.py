# Write a function that prints out nicely formatted information about a
# real estate listing. The information can vary for every listing, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

def real_add(num_rooms, num_bathrooms, area, intro, **kwargs):
    mult_feat = ""
    for k, v in kwargs.items():
        mult_feat += f"{k} - {v}" + "\n"
    return f"This lovely property in {area} has {num_rooms} bed rooms and {num_bathrooms} bath rooms.\n{intro}\nAdditional features include:\n{mult_feat}"

print(real_add(4, 2, "seaside", "This beachfront property would suit a couple of small family and has a view of the sea!", kitchen= "This kitchen has marble countertops and steel appliances", garden= "The garden is full lawned with no slope"))

