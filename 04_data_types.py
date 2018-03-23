# Booleans
  # => true or false
# Numbers
# Strings
# Bytes and byte arrays
# None

# => types used to manage data collection
# Lists
# Tuples
# Sets
# Dictionaries

meal_completed = True 
sub_total = 100
tip = sub_total * 0.2 # 20%
print(sub_total) # => 100
print(tip) # => 20.0
total = sub_total + tip
print(total) # => 120.0

receipt = "Your total is " + total 
print(receipt) # => Error TypeError
  # => string cannot be combined with a number

receipt = "Your total is " + str(total)
  # => converts total to string type
print(receipt) # => Your total is 120.0

