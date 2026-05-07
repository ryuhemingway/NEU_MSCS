import numpy as np
import matplotlib.pyplot as plt

# SECTION 2.1 — QUADRATIC FUNCTIONS

def f1(x):
    # f1(x) = x^2
    # this is a convex parabola with a minimum at x = 0
    return x ** 2

def deriv_f1(x):
    # exact derivative of f1(x) = x^2
    # f1'(x) = 2x
    return 2 * x

def f2(x):
    # f2(x) = x^2 - 2x + 3
    # this is a convex parabola with a minimum at x = 1
    return x ** 2 - 2 * x + 3

def deriv_f2(x):
    # exact derivative of f2(x) = x^2 - 2x + 3
    # f2'(x) = 2x - 2
    return 2 * x - 2

def gradient_descent(f, deriv_f, x0, alpha, epsilon, iter_max=1000):
    # implements the gradient descent algorithm for a 1 variable function
    # we pass in f and deriv_f as arguments so the function works for any function
    # iter tracks how many steps we take and stops us if we exceed iter_max

    x = x0
    iter = 0

    while iter < iter_max:
        x_new = x - alpha * deriv_f(x)
        if abs(x_new - x) < epsilon:
            x = x_new
            iter += 1
            break
        x = x_new
        iter += 1

    return x, iter

def plot_opt(f, x_opts, x_range, title, label_f, labels, colors):
    # plots the function as a blue curve and marks one or more minima
    # x_opts: list of optimal x values to plot
    # labels: list of legend labels for each point
    # colors: list of colors for each point

    x_vals = np.linspace(x_range[0], x_range[1], 500)
    y_vals = f(x_vals)

    plt.figure()
    plt.plot(x_vals, y_vals, label=label_f, color='blue')
    for i in range(len(x_opts)):
        plt.scatter([x_opts[i]], [f(x_opts[i])], color=colors[i], zorder=5,
                    label=labels[i])
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def section_2_1():
    # runs all hyperparameter tests for section 2.1

    print("SECTION 2.1 — QUADRATIC FUNCTIONS\n")

    # Part 1: Baseline test
    print("Part 1: Baseline test (x0=3, alpha=0.1, epsilon=0.001)\n")

    x_opt_f1, iters_f1 = gradient_descent(f1, deriv_f1, x0=3, alpha=0.1, epsilon=0.001)
    print("f1: optimal x = " + str(round(x_opt_f1, 6)) + ", iterations = " + str(iters_f1))

    x_opt_f2, iters_f2 = gradient_descent(f2, deriv_f2, x0=3, alpha=0.1, epsilon=0.001)
    print("f2: optimal x = " + str(round(x_opt_f2, 6)) + ", iterations = " + str(iters_f2))
    print()

    plot_opt(f1, [x_opt_f1], (-4, 4),
             "Gradient Descent on f1(x) = x^2", "f1(x) = x^2",
             ["Minimum: x* = " + str(round(x_opt_f1, 4))], ["red"])

    plot_opt(f2, [x_opt_f2], (-2, 5),
             "Gradient Descent on f2(x) = x^2 - 2x + 3", "f2(x) = x^2 - 2x + 3",
             ["Minimum: x* = " + str(round(x_opt_f2, 4))], ["red"])

    # Part 2: Varying x0
    print("Part 2: Varying x0 (alpha=0.1, epsilon=0.001)\n")
    print("Prediction: both x0 = +3 and x0 = -3 should converge to the same minimum.")
    print("Reason: f1 and f2 are convex parabolas so they each have only one global minimum.\n")

    x_f1_pos, i_f1_pos = gradient_descent(f1, deriv_f1, x0=3, alpha=0.1, epsilon=0.001)
    x_f1_neg, i_f1_neg = gradient_descent(f1, deriv_f1, x0=-3, alpha=0.1, epsilon=0.001)
    print("f1 with x0=+3: x* = " + str(round(x_f1_pos, 6)) + " (" + str(i_f1_pos) + " iters)")
    print("f1 with x0=-3: x* = " + str(round(x_f1_neg, 6)) + " (" + str(i_f1_neg) + " iters)")
    print()

    x_f2_pos, i_f2_pos = gradient_descent(f2, deriv_f2, x0=3, alpha=0.1, epsilon=0.001)
    x_f2_neg, i_f2_neg = gradient_descent(f2, deriv_f2, x0=-3, alpha=0.1, epsilon=0.001)
    print("f2 with x0=+3: x* = " + str(round(x_f2_pos, 6)) + " (" + str(i_f2_pos) + " iters)")
    print("f2 with x0=-3: x* = " + str(round(x_f2_neg, 6)) + " (" + str(i_f2_neg) + " iters)")
    print()

    print("Observation: both starting points converge to the same minimum.")
    print("This confirms our prediction that convexity guarantees a unique global minimum.\n")

    # Part 3: Varying alpha
    print("Part 3: Varying alpha (x0=3, epsilon=0.001)\n")

    x_a1, i_a1 = gradient_descent(f1, deriv_f1, x0=3, alpha=1, epsilon=0.001)
    print("alpha=1:      f1 -> x* = " + str(round(x_a1, 6)) + " (" + str(i_a1) + " iters)")

    x_a2, i_a2 = gradient_descent(f1, deriv_f1, x0=3, alpha=0.001, epsilon=0.001)
    print("alpha=0.001:  f1 -> x* = " + str(round(x_a2, 6)) + " (" + str(i_a2) + " iters)")

    x_a3, i_a3 = gradient_descent(f1, deriv_f1, x0=3, alpha=0.0001, epsilon=0.001)
    print("alpha=0.0001: f1 -> x* = " + str(round(x_a3, 6)) + " (" + str(i_a3) + " iters)")
    print()

    print("OBSERVATIONS:")
    print("alpha = 1: too large. The update rule gives x_new = x - 1*(2x) = -x.")
    print("Starting at x0=3: 3 -> -3 -> 3 -> -3 ... it oscillates and never converges.")
    print("It hits iter_max=1000 and stops without finding the minimum.")
    print()
    print("alpha = 0.001: too small. Each step is so tiny that |x_new - x| falls below epsilon while x is still far from the true minimum.")
    print()
    print("alpha = 0.0001: even smaller. The very first step (3 -> 2.9994) already has |x_new - x| = 0.0006 < epsilon = 0.001, so it stops after just 1 iteration.")
    print("The algorithm thinks it has converged but x* is still near the starting point.")
    print()
    print("Takeaway: alpha must be small enough to avoid overshooting but large enough to make meaningful progress before the stopping condition triggers.\n")

    # Part 4: Varying epsilon
    print("Part 4: Varying epsilon (x0=3, alpha=0.1)\n")

    x_e1, i_e1 = gradient_descent(f1, deriv_f1, x0=3, alpha=0.1, epsilon=0.1)
    print("epsilon=0.1:    f1 -> x* = " + str(round(x_e1, 6)) + " (" + str(i_e1) + " iters)")

    x_e2, i_e2 = gradient_descent(f1, deriv_f1, x0=3, alpha=0.1, epsilon=0.01)
    print("epsilon=0.01:   f1 -> x* = " + str(round(x_e2, 6)) + " (" + str(i_e2) + " iters)")

    x_e3, i_e3 = gradient_descent(f1, deriv_f1, x0=3, alpha=0.1, epsilon=0.0001)
    print("epsilon=0.0001: f1 -> x* = " + str(round(x_e3, 6)) + " (" + str(i_e3) + " iters)")
    print()

    print("OBSERVATIONS:")
    print("epsilon = 0.1: stops early, fast but imprecise, x* is far from the true minimum.")
    print("epsilon = 0.01: more precise, requires more iterations.")
    print("epsilon = 0.0001: most precise, requires the most iterations.")
    print("Takeaway: larger epsilon is faster but less accurate. Smaller epsilon is slower but more accurate.\n")


# SECTION 2.2 — MORE COMPLEX FUNCTIONS

def f3(x):
    # f3(x) = sin(x) + cos(sqrt(2) * x)
    # this function has multiple local minima unlike f1 and f2
    return np.sin(x) + np.cos(np.sqrt(2) * x)

def deriv_f3(x):
    # exact derivative of f3(x)
    # given in the assignment: f3'(x) = cos(x) - sqrt(2) * sin(sqrt(2) * x)
    return np.cos(x) - np.sqrt(2) * np.sin(np.sqrt(2) * x)

def plot_f3():
    # plots f3 over [0, 10] so we can see how many local minima it has

    x_vals = np.linspace(0, 10, 1000)
    y_vals = f3(x_vals)

    plt.figure()
    plt.plot(x_vals, y_vals, color='blue', label='f3(x) = sin(x) + cos(sqrt(2)*x)')
    plt.xlabel('x')
    plt.ylabel('f3(x)')
    plt.title('f3(x) on [0, 10]')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    print("f3(x) has approximately 3-4 local minima on [0, 10].")
    print("Because f3 is non-convex, gradient descent will find different local minima depending on where it starts.\n")

def section_2_2():
    # runs gradient descent on f3 from four different starting points

    print("SECTION 2.2 — COMPLEX FUNCTION f3\n")

    plot_f3()

    alpha = 0.1
    epsilon = 0.0001

    x_opt1, iters1 = gradient_descent(f3, deriv_f3, x0=1, alpha=alpha, epsilon=epsilon)
    x_opt4, iters4 = gradient_descent(f3, deriv_f3, x0=4, alpha=alpha, epsilon=epsilon)
    x_opt5, iters5 = gradient_descent(f3, deriv_f3, x0=5, alpha=alpha, epsilon=epsilon)
    x_opt7, iters7 = gradient_descent(f3, deriv_f3, x0=7, alpha=alpha, epsilon=epsilon)

    print("Gradient Descent on f3 for different starting points:\n")
    print("x0=1: x* = " + str(round(x_opt1, 4)) + ", f3(x*) = " + str(round(f3(x_opt1), 4)) + ", iters = " + str(iters1))
    print("x0=4: x* = " + str(round(x_opt4, 4)) + ", f3(x*) = " + str(round(f3(x_opt4), 4)) + ", iters = " + str(iters4))
    print("x0=5: x* = " + str(round(x_opt5, 4)) + ", f3(x*) = " + str(round(f3(x_opt5), 4)) + ", iters = " + str(iters5))
    print("x0=7: x* = " + str(round(x_opt7, 4)) + ", f3(x*) = " + str(round(f3(x_opt7), 4)) + ", iters = " + str(iters7))
    print()

    print("OBSERVATIONS:")
    print("x0=1 and x0=4 converge to the same local minimum.")
    print("x0=5 and x0=7 converge to a different local minimum.")
    print("This shows that for non-convex functions the starting point determines which local minimum is found. There is no guarantee of finding the global minimum.\n")

    # plot f3 with all four minima using the updated plot_opt function
    plot_opt(f3,
             [x_opt1, x_opt4, x_opt5, x_opt7],
             (0, 10),
             "Gradient Descent on f3: Local Minima from Different Starting Points",
             "f3(x)",
             ["x0=1 -> x*=" + str(round(x_opt1, 3)),
              "x0=4 -> x*=" + str(round(x_opt4, 3)),
              "x0=5 -> x*=" + str(round(x_opt5, 3)),
              "x0=7 -> x*=" + str(round(x_opt7, 3))],
             ["red", "green", "orange", "purple"])


# SECTION 3 — DERIVATIVE APPROXIMATION

def approx_deriv(f, x, h=1e-6):
    # approximates the derivative
    # f'(x) ≈ (f(x+h) - f(x)) / h 
    # h = 1e-7 is small enough to be accurate but not so small that rounding errors occur
    return (f(x + h) - f(x)) / h

def gradient_descent_approx(f, x0, alpha, epsilon, iter_max=1000):
    # same as gradient_descent() but uses approx_deriv instead of an exact derivative
    # this means it works for any function even if we cannot compute the derivative by hand

    x = x0
    iter = 0

    while iter < iter_max:
        grad = approx_deriv(f, x)
        x_new = x - alpha * grad
        if abs(x_new - x) < epsilon:
            x = x_new
            iter += 1
            break
        x = x_new
        iter += 1

    return x, iter

def section_3():
    # tests the derivative approximation and compares it to exact derivatives

    print("SECTION 3 — DERIVATIVE APPROXIMATION\n")

    # Part 1: check that approx_deriv is accurate
    print("Part 1: Comparing approx_deriv to exact derivatives\n")

    test_points = [-3, -1, 0, 1, 3]

    print("For f1(x) = x^2  [exact derivative: f1'(x) = 2x]")
    for x in test_points:
        exact = deriv_f1(x)
        approx = approx_deriv(f1, x)
        diff = abs(exact - approx)
        print("x=" + str(x) + ":  exact=" + str(round(exact, 8)) + "  approx=" + str(round(approx, 8)) + "  difference=" + str(round(diff, 10)))

    print()
    print("For f2(x) = x^2 - 2x + 3  [exact derivative: f2'(x) = 2x - 2]")
    for x in test_points:
        exact = deriv_f2(x)
        approx = approx_deriv(f2, x)
        diff = abs(exact - approx)
        print("x=" + str(x) + ":  exact=" + str(round(exact, 8)) + "  approx=" + str(round(approx, 8)) + "  difference=" + str(round(diff, 10)))

    print("Observation: the differences are extremely small (around 1e-6). Therefore the approximation is accurate.\n")

    # Part 2: run gradient descent using the approximation and compare to exact
    print("Part 2: Gradient descent using approximate derivative\n")
    print("Testing on f1 and f2 with x0=3, alpha=0.1, epsilon=0.001\n")

    x_exact_f1, i_exact_f1 = gradient_descent(f1, deriv_f1, x0=3, alpha=0.1, epsilon=0.001)
    x_approx_f1, i_approx_f1 = gradient_descent_approx(f1, x0=3, alpha=0.1, epsilon=0.001)
    print("f1 exact derivative:  x* = " + str(round(x_exact_f1, 6)) + " (" + str(i_exact_f1) + " iters)")
    print("f1 approx derivative: x* = " + str(round(x_approx_f1, 6)) + " (" + str(i_approx_f1) + " iters)")
    print()

    x_exact_f2, i_exact_f2 = gradient_descent(f2, deriv_f2, x0=3, alpha=0.1, epsilon=0.001)
    x_approx_f2, i_approx_f2 = gradient_descent_approx(f2, x0=3, alpha=0.1, epsilon=0.001)
    print("f2 exact derivative:  x* = " + str(round(x_exact_f2, 6)) + " (" + str(i_exact_f2) + " iters)")
    print("f2 approx derivative: x* = " + str(round(x_approx_f2, 6)) + " (" + str(i_approx_f2) + " iters)")
    print()

    print("Conclusion: both versions give the same results.")
    print("The approximation is accurate enough that it does not affect gradient descent.")
    print("This means we can use approx_deriv for any function without needing to compute the derivative by hand.\n")


# SECTION 4 — GRADIENT DESCENT FOR TWO VARIABLES

def approx_partial_x(f, x, y, h=1e-7):
    # approximates the partial derivative of f with respect to x
    # we will nudge x by a small amount h and hold y constant
    return (f(x + h, y) - f(x, y)) / h

def approx_partial_y(f, x, y, h=1e-7):
    # approximates the partial derivative of f with respect to y
    # we will nudge y by a small amount h and hold x constant
    return (f(x, y + h) - f(x, y)) / h

def gradient_descent_2d(f, x0, y0, alpha, epsilon, iter_max=1000):
    # gradient descent for a two variable function f(x, y)
    # same logic as the 1D version but now we update both x and y each iteration
    # we want to stop when both x and y have converged

    x = x0
    y = y0
    iter = 0

    while iter < iter_max:
        grad_x = approx_partial_x(f, x, y)
        grad_y = approx_partial_y(f, x, y)

        x_new = x - alpha * grad_x
        y_new = y - alpha * grad_y

        # both x and y must converge before we stop
        if abs(x_new - x) < epsilon and abs(y_new - y) < epsilon:
            x = x_new
            y = y_new
            iter += 1
            break

        x = x_new
        y = y_new
        iter += 1

    return x, y, iter

def f_2d_bowl(x, y):
    # f(x, y) = x^2 + y^2
    # minimum is at (0, 0)
    return x ** 2 + y ** 2

def plot_2d_opt(f, x_opt, y_opt, x_range, y_range, title):
    # creates a 3D surface plot and marks the minimum with a red dot.

    x_vals = np.linspace(x_range[0], x_range[1], 100)
    y_vals = np.linspace(y_range[0], y_range[1], 100)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = f(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, alpha=0.6, cmap='jet')
    ax.scatter([x_opt], [y_opt], [f(x_opt, y_opt)], color='red', s=100,
               label='minimum: (' + str(round(x_opt, 3)) + ', ' + str(round(y_opt, 3)) + ')')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    ax.set_title(title)
    ax.legend()
    plt.tight_layout()
    plt.show()

def section_4():
    # tests gradient descent on the 2D bowl function

    print("SECTION 4 — GRADIENT DESCENT FOR TWO VARIABLES\n")

    print("Test: f(x,y) = x^2 + y^2  (true minimum at (0, 0))\n")
    x_opt, y_opt, iters = gradient_descent_2d(f_2d_bowl, x0=3, y0=3, alpha=0.1, epsilon=0.001)
    print("Result: x* = " + str(round(x_opt, 6)) + ", y* = " + str(round(y_opt, 6)) + ", iters = " + str(iters))
    print("True minimum is (0, 0). Our result is close within the tolerance epsilon=0.001.\n")
    plot_2d_opt(f_2d_bowl, x_opt, y_opt, (-4, 4), (-4, 4), 'GD on f(x,y) = x^2 + y^2')

# MAIN

def main():
    print("PROJECT 1 | PART 1\n")
    section_2_1()
    section_2_2()
    section_3()
    section_4()


if __name__ == "__main__":
    main()