# 2. WRITE A FOR LOOP THAT LOOPS OVER DATA AND PRINTS THE SUM OF EACH
#  NESTED TUPLE. THE OUTPUT SHOULD LOOK LIKE THIS
# Row 1 sum: 3
# Row 2 sum: 7
nested = ((1,2), (3,4))
print(nested)

for i in range(len(nested)):
    print(f"Row {i + 1} sum: {sum(nested[i])}")

nested_copy = nested[:]
print(nested_copy)

numbers = [5, 3, 8, 1]
numbers.sort() 
print(numbers)
