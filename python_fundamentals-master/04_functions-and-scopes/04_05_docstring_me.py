# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    """Function converts kilometers to miles

    Args:
        km (int): the amount of km you want to convert to miles

    Returns:
        int: amount of miles converted from km
    """
    miles = km * 0.6
    return miles

print(km_to_miles.__doc__)
