def combs(i, k):
  items = list(i)

  if k == 0:
    # Choosing 0 items returns a list containing an empty list// an empty set
    return [[]]

  if len(items) == 0:
    # No items to choose from returns a empty list
    return []

  if k > len(items):
    # No combinations possible as you can't choose more items than there exists
    return []

  # Storing the first element
  i1 = items[0]

  # Storing the rest of the elements of the list
  r = items[1:]

  # Combinations with the first element
  c1 = []

  # Temporary list with the combinations without the first element and with 1 less than the necessary amount
  temp = combs(r, k - 1)

  for combo in temp:
    # Adds the first element and the temporary list with combinations without the first element into the list of combinations with the first element
    c1.append([i1] + combo)

  # Combinations without the first element
  c0 = combs(r, k)

  return c0 + c1

print("Combinations of [5, 14, 25] choosing 1: ")
print(combs([5, 14, 25], 1))

print("Combinations of [5, 14, 25] choosing 2: ")
print(combs([5, 14, 25], 2))

print("Combinations of [5, 14, 25] choosing 3: ")
print(combs([5, 14, 25], 3))