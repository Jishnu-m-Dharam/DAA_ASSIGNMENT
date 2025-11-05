def hack(otp):
    current = 1000
    while current <= 9999:
        if current == otp:
            print(f"OTP hacked successfully!", "it is ", {current})
            return True
        current += 1
    return False

otp = int(input("Enter the 4-digit OTP to hack: "))
hack(otp)