# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(list_):
  max_val = max(list_)
  min_val = min(list_)
  avg_val = sum(list_) / len(list_)
  return f"max = {max_val}, min = {min_val}, average = {avg_val}"

# call the function below here
print(stats(example_list))