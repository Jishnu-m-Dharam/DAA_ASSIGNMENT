s = input("Enter a string:")
search_s="the"
indices = []
i=0
while i < len(s):
    if s[i:i+len(search_s)] == search_s:
        indices.append(i)
    i += 1
print("The indices of 'the' is: ",indices)

