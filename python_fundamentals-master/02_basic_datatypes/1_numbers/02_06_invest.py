'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
# Define variables
a = float(input("How much can you invest? "))
b = float(input("what is your interest rate in % ? ")) / 100
c = float(input("how many years can you invest for? "))

# Formula
d = round(a * ((1+(b/1))**c),2)
print("your future investment will be worth " + str(d))
