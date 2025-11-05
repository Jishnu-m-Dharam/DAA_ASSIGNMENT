
import math

def distance(p1, p2):
  x_dist = p1[0] - p2[0]
  y_dist = p1[1] - p2[1]

  return (x_dist**2 + y_dist**2)**0.5

def bruteForce(points):
  min_dist = float('inf')
  best_pair = (None, None)
  n = len(points)

  for i in range(n):
    for j in range(i + 1, n):
      d = distance(points[i], points[j])
      if d < min_dist:
        min_dist = d
        best_pair = (points[i], points[j])

  return min_dist, best_pair

def closestRecursive(points_sorted):
  n = len(points_sorted)
  if n <= 3:
    return bruteForce(points_sorted)

  mid_index = n // 2
  left = points_sorted[:mid_index]
  right = points_sorted[mid_index:]

  mid_line = points_sorted[mid_index - 1][0]

  (d1, pair1) = closestRecursive(left)
  (d2, pair2) = closestRecursive(right)

  if d1 < d2:
    temp = d1
    best_pair = pair1
  else:
    temp = d2
    best_pair = pair2

  # Points in the original list that are within the minimum distance of the dividing line
  strip = [p for p in points_sorted if abs(p[0] - mid_line) < temp]

  # Sorting the strip by the y-coordinates
  strip.sort(key = lambda p: p[1])

  # Best pair in the (y-sorted) strip
  min_dist_strip = temp
  best_pair_strip = best_pair

  n_strip = len(strip)
  for i in range(n_strip):
    for j in range(i + 1, n_strip):
      # If y-distance is greater than the minimum distance of the strip break the loop as the rest of the list will only contain greater values
      if (strip[j][1] - strip[i][1]) >= min_dist_strip:
        break

      d_strip = distance(strip[i], strip[j])
      if d_strip < min_dist_strip:
        min_dist_strip = d_strip
        best_pair_strip = (strip[i], strip[j])

  if min_dist_strip < temp:
    return min_dist_strip, best_pair_strip
  else:
    return temp, best_pair

def closestPair(points):
  if len(points) < 2:
    return float('inf'), (None, None)

  # Sorting points by the x-coordinates
  points_sorted = sorted(points, key = lambda p: p[0])

  min_dist, pair = closestRecursive(points_sorted)
  return min_dist, pair

points = [
    (2, 3), (12, 30), (40, 50), (5, 1),
    (12, 10), (6, 7), (1, 100), (4, 4)
]

min_distance, pair = closestPair(points)

print(f"Points: {points}")
print("---")
print(f"Closest pair: {pair}")
print(f"Minimum distance: {min_distance:.4f}")