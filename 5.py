def knapsack():
  # Items consist of a weight and value in a tuple
  items = [(5, 60), (3, 50), (4, 70), (2, 30), (1, 25), (6, 90)]

  # Maximum number of items that can be held
  max = 10
  num = len(items)

  # Best value to pick up
  bv = 0
  # Best weight to pick up
  bw = 0
  # Best combination of value and weight to pick up
  bc = ""

  # Total number of combinations
  nCombs = 2**num

  print(f"Total items: {num}")
  print(f"Knapsack Capacity: {max}")
  print(f"Total Combinations: {nCombs}")

  for i in range(nCombs):
    # Creating a 6-bit binary string for i
    bStr = format(i, f'0{num}b')

    cv = 0
    cw = 0

    for j in range(num):
      # Checking if j-th bit is 1
      if bStr[j] == '1':
        # Taking the value if it is 1
        weight, value = items[j]
        cw += weight
        cv += value

    # If current weight is under or equal to max capacity
    if cw <= max:
      # If current value is greater than the best value
      if cv > bv:
        # Change the best value, weight and the combination of the two to be updated
        bv = cv
        bw = cw
        bc = bStr

  print(f"Binary Representation: {bc}")
  print("Items to Take (Item 0 is first, Item 5 is last):")

  # Printing out the items in the best combination
  taken_items = []
  for k in range(num):
      if bc[k] == '1':
          taken_items.append(f"Item {k} {items[k]}")

  print("  " + "\n  ".join(taken_items))
  print(f"\nTotal Weight: {bc} (Capacity: {max})")
  print(f"Total Value: {bv}")


knapsack()
     