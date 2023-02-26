def bplOvers(T):
    outcomes = ['O', '1', '2', '3', '4', '5', '6']

    for i in range(T):
        string = input("Enter Over Details ")

        legalDeliveries = 0

        for letter in string:
            if letter in outcomes:
                legalDeliveries += 1

        overs = int(legalDeliveries / 6)
        balls = legalDeliveries % 6

        overUnit = "OVER"
        ballUnit = "BALL"

        if overs > 1:
            overUnit = "OVERS"

        if balls > 1:
            ballUnit = "BALLS"

        if(overs >= 1 and balls >= 1):
            print(f"{str(overs)} {overUnit} {str(balls)} {ballUnit}")

        if(overs >= 1 and balls == 0):
            print(f"{str(overs)} {overUnit}")

        if(overs == 0 and balls >= 0):
            print(f"{str(balls)} {ballUnit}")


print(bplOvers(3))
