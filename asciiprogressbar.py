def asciiProgressBar(percentage):
    digits = [*str(int(percentage))]

    if percentage >= 0 and percentage <= 100:
        if len(digits) > 2 and digits[0] == "1":
            digit = int(digits[0] + "0")
        else:
            digit = int(digits[0])

        bar = digit * "+" + (10 - digit) * "."
        rounded = digit * 10

        return "[" + bar + "]" + " " + str(rounded) + "%"
    else:
        return "Invalid input"


print(asciiProgressBar(78.8))
