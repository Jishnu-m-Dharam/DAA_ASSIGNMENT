def karatsuba(num1, num2):
   #if its less than 10 just do normal multiplication
    if num1 < 10 or num2 < 10:
        return num1 * num2

    #find the length of the numbers.
    size_of_value = max(len(str(num1)), len(str(num2)))
    half = size_of_value // 2

    # Split The Numbers Into Two Parts To Make It Easier
    High_num1 = num1 // 10**half
    low_num1 = num1 % 10**half
    high_num2 = num2 // 10**half
    low_num2 = num2 % 10**half

    #computing three products to use for karutsuba
    low_num1_2 = karatsuba(low_num1, low_num2)# Low part multiplication
    cross = karatsuba((low_num1 + High_num1), (low_num2 + high_num2))# Cross terms
    high_num1_2 = karatsuba(High_num1, high_num2)# High part multiplication

    # Combining The Products of all three values collected To Do Karutsuba Algorithm.
    return (high_num1_2 * 10*(2 * half)) + ((cross - high_num1_2 -low_num1_2) * 10*half) + low_num1_2


# Multiplication Of The Two Numbers Given
x = 1200
y = 4000

print("Multiplying Using Karatsuba:\nA=",x ,"B=",y,"\n\nResult:\n")

print(karatsuba(x, y))
     