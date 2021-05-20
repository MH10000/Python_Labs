'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]
# Create function
def stats(list_):
  print("Min: ", min(list_))
  print("Max: ", max(list_))
  print("Sum: ", sum(list_))
  print("Average: ", sum(list_) / len(list_))
  pass

# call the function below here
stats(example_list)