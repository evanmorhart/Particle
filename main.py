def SolveLinear(x0, v0, a, t):
    positionterm = x0
    velocityterm = v0 * t
    accelterm = 0.5 * a * t * t

    return postionterm + velocityterm + accelterm


def main():
    # Begin by collecting all variables

    x0 = input("Initial Initial Position: ")
    v0 = input("Enter Initial Velocity: ")
    a = input("Enter Acceleration: ")
    t = input("Enter desired time: ")

    x0 = float(x0)
    v0 = float(v0)
    a = float(a)
    t = float(t)

    solution = SolveLinear(x0, v0, a, t)

    print("The distance at a time " + str(t) + " is " + str(solution))

    return 0


if __name__ == "__main__":
    main()
