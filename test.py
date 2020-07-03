try:
    quotient = 0/0  # since this is impossible, it will except
    print(quotient)

except ZeroDivisionError as e:
    print("You cant divide by 0")


else:
    print("You were successful.")
