def perm(items):
    # Returns the item if the list length is less than or equal to one.
    if len(items) <= 1:
        return [items]

    perms = []

    # Storing the first element.
    i1 = items[0]

    # Recursively calling all elements after the first element.
    pr = perm(items[1:])

    for permutations in pr:
        for j in range(len(permutations) + 1):
            # Adding i1 / first element into different positions by manipulating the list
            np = permutations[:j] + [i1] + permutations[j:]
            # Adding this new permutation to the list of all permutations
            perms.append(np)

    return perms


def tsp():
  # Map of cities and indices
  cities = {
      'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4
  }

  # List of city names
  cityNames = ['A', 'B', 'C', 'D', 'E']

  # Matrix for distance
  distances = [
      [0, 10, 20, 30, 40],
      [10, 0, 15, 25, 35],
      [20, 15, 0, 12, 22],
      [30, 25, 12, 0, 18],
      [40, 35, 22, 18, 0]
      ]

  start = 'A'

  # Creates a list with all cities except the start city
  others = [city for city in cityNames if city != start]
  # also the same as:
  '''
  others = []
  for city in cityNames:
    if city != start:
      others.append(city)
  '''

  # Setting minimum total distance to infinite
  min = float('inf')
  best = []

  # Generating paths between the start and end nodes
  mid = perm(others)

  for permPath in mid:
    current = 0

    # Saves a full travel from start position back to start position
    cPathCity = [start] + permPath + [start]

    for i in range(len(cPathCity) - 1):
      # Saving the city names of the current and next cities
      c1n = cPathCity[i]
      c2n = cPathCity[i + 1]

      # Finding the index of the city names
      c1i = cities[c1n]
      c2i = cities[c2n]

      # Distance between the cities
      current += distances[c1i][c2i]

      # Checking if the current distance is less than the minimum total distance to find the best path
      if current < min:
        min = current
        best = cPathCity


  print(f"Best path: {'->'.join(best)}")
  print(f"Minimum distance: {min}")

tsp()