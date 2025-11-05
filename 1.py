def perm(i):
    items = list(i)
    # Returns the item if the list length <= 1
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


print("Permutations of the list [5, 16, 13, 15]: ")
print(perm([5, 16, 13, 15]))