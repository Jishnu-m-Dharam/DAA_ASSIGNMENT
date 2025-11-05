import random

def binCheck(num):
  # Converting an integer to a binary string using bin function and dropping the first two elements of the string 0b
  bString = bin(num)[2:] # Corrected slicing to get the binary string without '0b'

  if len(bString) == 0:
    print("Binary not found.")
    return

  # Creating a random number between 1 and the max length of the binary string (-1 because index starts from 0)
  r = random.randint(0, len(bString) - 1)

  bit = bString[r]

  # Cool way to write single line if statements
  result = "True" if bit == '1' else "False"

  print("Number: ", num)
  print("Binary: ", bString)
  print("Random index taken: ", r)
  print("Bit at the index:", bString[r])
  print("Result: ", result)


c = int(input("Enter a number to check a random digit of it's binary form: "))
binCheck(c)