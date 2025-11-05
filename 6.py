def combs(items, k):
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

def knapsack():
  # Items consist of a weight and value in a tuple
  items = [(5, 60), (3, 50), (4, 70), (2, 30), (1, 25), (6, 90)]

  # Maximum number of items that can be held
  max = 10
  num = len(items)

  iIndex = list(range(num))

  # Best value to pick up
  bv = 0
  # Best weight to pick up
  bw = 0
  # Best combination of value and weight to pick up
  bci = []


  # Looping through all combinations
  for k in range(1, num + 1):
    # Storing all combinations of length k
    all = combs(iIndex, k)

    for combos in all:
      cw = 0
      cv = 0

      for ind in combos:
        weight, value = items[ind]
        cw += weight
        cv += value

      if cw <= max:
        if cv > bv:
          # Updates the best values
          bv = cv
          bw = cw
          bci = combos
  print(f"Best combination was: {bci}")
  print("Items to Take:")

  for k in bci:
      print(f"  - Item {k} {items[k]}")

  print(f"\nTotal Weight: {bw} (Capacity: {max})")
  print(f"Total Value: {bv}")

knapsack()
