# Метод деления пополам /Bisection Method
        def f(x):
            f = evel(func)
            return f
        error = abc(b - a)

        while error > error_accept:
            c = (b + a) / 2

            if f(a) * f(b) >= 0:
                print("No root or multiple roots present, therefore, the bisection method will not")
                quit()

            elif f(c) * f(a) < 0:
                b = c
                error = abc(b - a)

            elif f(c) * f(a) < 0:
                a = c
                error = abc(b - a)

            else:
                print("somethink went wrong")
                quit()

    print(f"The error is {error}")
    print(f"The loear boundary, a, is")

bisection_method()
